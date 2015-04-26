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
#screen_x=1200
#screen_y=700

score = 0
current_level=0 # define global in the functions where you want to update this variable
level_transition=False

life = 6
Gameover=False

e=0
#====================================================



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
  background_image=pygame.transform.scale(background_image, (background_image.get_width(), screen_y)) 
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
      
  #====================================================
class Enemy(object):
  def __init__(self):
    self.x, self.y = 0,0
    self.valid = True
    self.score = 0 
    self.color = c.color[random.randrange(0,len(c.color))] # put a random number here between number of colours
    #self.e = 0
  def make_target(self):
    global current_level, level_transition,e
    self.x, self.y = screen_x,random.randrange(40,screen_y-100)
    self.valid = True
    self.color = c.color[random.randrange(0,len(c.color))] # put a random number here between number of colours
    e = e+1
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

def display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object,target_image):
  s="Marks-"+str(score)
  scoresurf,scoreRect=msg_text(s,800,40)
  DISPLAYSURF.blit(scoresurf, scoreRect)
  lev="Level-"+str(current_level+1)
  levsurf,levRect=msg_text(lev,400,40)

  l="Attempts-"+str(life)
  lifesurf,lifeRect=msg_text(l,600,40)
  
  
  player.handle_event(event,current_level)
  #DISPLAYSURF.blit(target_surf, target_xy)
  DISPLAYSURF.blit(infoSurf, infoRect)
  
  #DISPLAYSURF.blit(scoresurf, scoreRect)
  DISPLAYSURF.blit(levsurf,levRect)
  DISPLAYSURF.blit(lifesurf,lifeRect)
  
  DISPLAYSURF.blit(player.image, player.rect)
  
  
  
  
  
  
  
  for j in range(len(fire_object)):
    if fire_object[j].x!=sourcex:
      pygame.draw.circle(DISPLAYSURF, c.RED, (fire_object[j].x,fire_object[j].y), 8, 0)


  #pygame.draw.rect(DISPLAYSURF,target.color,(target.x,target.y,24,24))
  for i in range(len(target)):
    DISPLAYSURF.blit(target_image [i], (target_xy [0],target_xy [1]+ 24))
  
  
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
  global e
  resolution = display.Display().screen().root.get_geometry()
  screen_x, screen_y = resolution.width, resolution.height
  print screen_x, screen_y
  
  screen_x, screen_y = resolution.width, resolution.height
  
  #================define terminal size================
  DISPLAYSURF = display_init()
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
  
  
  #counter_target_move = 0
  counter_target_move = []
  target=[]
  target_surf=[]
  target_image=[]
  target_xy=[]
  e=0
  
  #====================================================
  for t in range(random.randrange(2,4)):
    target.append(Enemy())
    target_image.append(None)
    target_surf.append(0)
    target_xy.append(0)
    counter_target_move.append(0)
  

  #target = Enemy()
  
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
	target_surf[tar],target_xy[tar]=msg_text(c.exam[target[tar].ee],target [tar].x,target [tar].y)
	
	
	
	
	if (counter_target_move[tar] <3):
	  target_image[tar] = pygame.image.load(c.enemy_image_1 [target[tar].ee]).convert()
	  counter_target_move[tar] += 1
	else:
	  target_image[tar] = pygame.image.load(c.enemy_image_2 [target[tar].ee]).convert()
	  if (counter_target_move [tar] == 6):
	    counter_target_move[tar] =0
	  else:
	    counter_target_move[tar] += 1
	#target_image = pygame.image.load(c.enemy_image_1 [0]).convert()
	target_image [tar] = pygame.transform.scale2x(target_image)
	target_height[tar] = target_image.get_height();
	#DISPLAYSURF.blit(target_image, (targetx,targety))
      
	

	for fire in fire_object:
	    if fire.valid:
	      fire.fire_now()
	      if fire.x < target[tar].x+24 and fire.x > target[tar].x and fire.y < target[tar].y+ target_height[tar] and fire.y > target[tar].y:
		fire.destroy_fire(fire_object)
		target_surf[tar],target_xy[tar]=msg_text('destroyed',target[tar].x,target[tar].y)
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
	      
	      
	      
		    
	    if event.key==pygame.K_DOWN:
	      sourcey+=24
	      if sourcey>screen_y-50:
		sourcey=screen_y-50
	    if event.key==pygame.K_UP:
	      sourcey-=24
	      if sourcey<10:
		sourcey=10
      
    target_image.set_colorkey(c.BLACK)
    display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object, target_image)
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
    pygame.display.flip()

main()