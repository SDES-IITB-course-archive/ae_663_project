import pygame, sys
from Xlib import display
import random
from pygame.locals import *
from pygame.transform import scale
import math,subprocess
import os
import serge
import constant as c
target_object=[]



#============Global Variables========================


score = 0
current_level=0 # define global in the functions where you want to update this variable
level_transition=False

life = 6
Gameover=False

e=0
#====================================================


# do something
  #====================================================
def display_init():
  pygame.init()
  print screen_x,screen_y
  DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)
  pygame.display.set_caption(c.terminal_name)
  return DISPLAYSURF
  #====================================================
  
  #====================================================
def msg_text(text,x,y):  
 FONT = pygame.font.Font('freesansbold.ttf', 16)
 Surf = FONT.render(text, 1, c.WHITE)
 Rect = Surf.get_rect()
 Rect.topleft = (x, y - 25) 
 return Surf,Rect
  #====================================================




def background_image_set (DISPLAYSURF, background_image, x_y_start_pos):
  DISPLAYSURF.blit (background_image, x_y_start_pos)
  return DISPLAYSURF



  #====================================================
  #====================================================

  #====================================================
class make_fire(object):
  def __init__(self,sourcex,sourcey):
      self.x, self.y = sourcex + c.fire_starting_shift_x, sourcey + c.fire_starting_shift_y
      self.valid=True
      self.screen_x=screen_x
  
  def fire_load(self):
      return self.x,self.y
  
  def fire_now(self):
    if self.valid:
      self.x+=5
  def destroy_fire(self,fire_object):
    fire_object.remove(self)

class audio(object):
  def __init__(self):
    pass
	      
  def fire(self):
    pygame.mixer.music.load("sounds/fireball.ogg")
    pygame.mixer.music.play()
  
  def destroy(self):
    pygame.mixer.music.load("sounds/destroy.wav")
    pygame.mixer.music.play()
  def level_complete(self,fire_object):
    pygame.mixer.music.load("sounds/fireball.ogg")
    pygame.mixer.music.play()
  def game_over(self):
    pygame.mixer.music.load("sounds/fireball.ogg")
    pygame.mixer.music.play()
  #====================================================
class Enemy(object):
  def __init__(self):
    self.x, self.y = 0,0
    self.valid = True
    self.score = 0 
    self.color = c.color[random.randrange(0,len(c.color))] # put a random number here between number of colours

  def make_target(self):
    global current_level,level_transition,e
    self.x, self.y = screen_x,random.randrange(40,screen_y-100)
    self.valid = True
    self.color = c.color[random.randrange(0,len(c.color))] # put a random number here between number of colours
    e += 1
    self.ee=e
    if self.ee>len(c.exam)-1:
      self.ee=0
      e=0
      current_level=current_level+1
      level_transition=True
      if current_level>len(c.level)-1:
	current_level=0
    self.score = c.score[e]
  def move_target(self):
    if self.valid:
      self.x-=5

      
  def destroy_target(self,fire_object):
    target_object.pop(k)
    score+= self.score
    
  #====================================================


    
  #====================================================
def get_resolution():
  resolution = display.Display().screen().root.get_geometry()
  return resolution.width, resolution.height
  
def display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object):
  s="Marks-"+str(score)
  scoresurf,scoreRect=msg_text(s,800,40)
  DISPLAYSURF.blit(scoresurf, scoreRect)
  lev="Level-"+str(current_level+1)
  levsurf,levRect=msg_text(lev,400,40)

  l="Attempts-"+str(life)
  lifesurf,lifeRect=msg_text(l,600,40)

  
  player.handle_event(event,current_level)
  DISPLAYSURF.blit(infoSurf, infoRect)

  
  
  DISPLAYSURF.blit(levsurf,levRect)
  DISPLAYSURF.blit(lifesurf,lifeRect)
  

  DISPLAYSURF.blit(player.image, player.rect)
  
   #========= Target image selection========
  #target_image = pygame.image.load(c.target_image_list [color_counter]).convert()
  #target_image = pygame.transform.scale(target_image, (c.target_width, c.target_height))
  #pygame.draw.circle(surface, color, center_point, radius, width)
  for j in range(len(fire_object)):
    if fire_object[j].x!=sourcex:
      pygame.draw.circle(DISPLAYSURF, c.RED, (fire_object[j].x,fire_object[j].y), 8, 0)


  for i in range(len(target)):
    pygame.draw.rect(DISPLAYSURF,target[i].color,(target[i].x,target[i].y,24,24))
    DISPLAYSURF.blit(target_surf[i], target_xy[i])


  clock.tick(c.tick[c.level[current_level]])
  pygame.display.update()
  #====================================================
  
  #====================================================
def main():
  global score
  global Gameover
  global life
  global level_transition
  global screen_x
  global screen_y
  sound = audio()
  screen_x, screen_y = get_resolution()
  #================define terminal size================
  DISPLAYSURF = display_init()
  #audio_init()
  #====================================================
  
  #================define Local Variables================

  sourcex = 10
  sourcey = 10
  fire_object=[]
  player = serge.Serge((sourcex, sourcey))
  clock=pygame.time.Clock()
  target_delay=0
  
  x_back_ground_start=0
  y_back_ground_start=0
  
  background_counter=0
  
  target=[]
  target_surf=[]
  target_xy=[]
  #====================================================
  for t in range(random.randrange(2,4)):
    target.append(Enemy())
    target_surf.append(0)
    target_xy.append(0)
  

  #========================the main game loop========================
  while not Gameover:
    sourcex = player.rect[0]
    sourcey = player.rect[1]
    lev_delay=c.level_delay
    
    while level_transition:
      while lev_delay>0:
	lev_delay=lev_delay-1
        DISPLAYSURF.fill(c.BLACK)
        level_msg="Level:"+str(current_level+1)
        lifesurf,lifeRect=msg_text(level_msg,screen_x/2,screen_y/2)
	DISPLAYSURF.blit(lifesurf,lifeRect)
        pygame.display.flip()
      level_transition=False

    
    #=======================Background Image=======================

    if current_level==background_counter:
      e=0
      fire_object=[]
      background_counter=(background_counter+1)
      background_image = pygame.image.load(c.image_name[current_level]).convert()
      DISPLAYSURF=background_image_set (DISPLAYSURF, background_image,[x_back_ground_start,y_back_ground_start])
      if background_counter==len(c.level):
	background_counter=0
    
    #===============Moving the Background===========================
    x_back_ground_start = x_back_ground_start - c.background_speed [current_level]
    DISPLAYSURF=background_image_set (DISPLAYSURF, background_image, [x_back_ground_start, y_back_ground_start])
    
   
   #================================================================
    
    infoSurf,infoRect=msg_text(c.terminal_name,10,screen_x)
    
    if target_delay>0:
      target_delay=target_delay-1
    else:
      for tar in range(len(target)):
	target[tar].x-=5
	if target[tar].x<0:
	  target[tar].make_target()
	  life-=1
	  if life==0:
	    Gameover=True
	target_surf[tar],target_xy[tar]=msg_text(c.exam[target[tar].ee],target[tar].x,target[tar].y)
	
	


	for fire in fire_object:
	  if fire.valid:
	    fire.fire_now()
	    if fire.x < target[tar].x+24 and fire.x > target[tar].x and fire.y < target[tar].y+24 and fire.y > target[tar].y:
	      fire.destroy_fire(fire_object)
	      target_surf[tar],target_xy[tar]=msg_text('destroyed',target[tar].x,target[tar].y)
	      sound.destroy()
	      target_delay=c.delay[current_level]
	      target[tar].make_target()
	      score+= target[tar].score
	      
	      
	    if fire.x >= screen_x:
	      fire.destroy_fire(fire_object)
	      
	
	
	for event in pygame.event.get():
	  if event.type == QUIT:
	    pygame.quit()
	    sys.exit()
	    
	  if event.type==pygame.KEYDOWN:
	    if event.key==pygame.K_f:
	      fire_object.append(make_fire(sourcex,sourcey))
	      sound.fire()
	      
	      
	      
		    
	    if event.key==pygame.K_DOWN:
	      sourcey+=24
	      if sourcey>screen_y-50:
		sourcey=screen_y-50
	    if event.key==pygame.K_UP:
	      sourcey-=24
	      if sourcey<10:
		sourcey=10
  
    
    display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object)

  #==================================================================
  
  while Gameover:
    DISPLAYSURF.fill(c.BLACK)
    lifesurf,lifeRect=msg_text("Game Over",screen_x/2,screen_y/2)
    
    for event in pygame.event.get():
	if event.type == QUIT:
	  pygame.quit()
	  sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Gameover = False
	  
    DISPLAYSURF.blit(lifesurf,lifeRect)
    #pygame.display.flip()

main()
