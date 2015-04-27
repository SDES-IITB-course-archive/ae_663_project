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

Game_start=False

e=0
#====================================================


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
def msg_text(text,x,y,txt_color=c.WHITE,size=16):  
 FONT = pygame.font.Font('freesansbold.ttf', size)
 Surf = FONT.render(text, 1, txt_color)
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
class make_target(object):
  def __init__(self):
    global current_level,level_transition,e,life
    self.x, self.y = screen_x,random.randrange(40,screen_y-100)
    self.valid = True
    self.score = c.score[e]
    self.image1 = c.enemy_image_1[e]
    self.image2 = c.enemy_image_2[e]
    self.image = pygame.image.load(self.image1).convert()
    self.image = pygame.transform.scale2x(self.image)
#target_height[tar] = self.image.get_height();
    self.surf,self.xy=msg_text(c.exam[e],self.x, self.y)
    self.image_counter = 0
    self.height = self.image.get_height()
    self.e1 = e
    e += 1

  def move_target(self,target_object):
    global current_level,level_transition,e,life
    if self.valid:
      self.x-=5
      self.surf,self.xy=msg_text(c.exam[self.e1],self.x, self.y)
      if self.x<0:
	  self.destroy_target(target_object)
	  life-=1
	  if life==0:
	    Gameover=True
      if (self.image_counter <3):
	  self.image = pygame.image.load(self.image1).convert()
      else:
	  self.image = pygame.image.load(self.image2).convert()
      self.image_counter = (self.image_counter + 1)%6	
      self.image = pygame.transform.scale2x(self.image)
      self.image.set_colorkey(c.BLACK)
	
      
  def destroy_target(self,target_object):
    global current_level,level_transition,e
    target_object.remove(self)
    print e, len(c.exam) , len(target_object)
    if(e == len(c.exam) and len(target_object) == 0):
      current_level += 1
      level_transition = True
      e = 0
    
    
  #====================================================

def get_resolution():
  resolution = display.Display().screen().root.get_geometry()
  return resolution.width, resolution.height

  #====================================================

  #====================================================
def display_score(score, DISPLAYSURF):
  s="Marks-"+str(score)
  scoresurf,scoreRect=msg_text(s,800,40)
  DISPLAYSURF.blit(scoresurf, scoreRect)
def display_level(current_level,DISPLAYSURF):
  lev="Level-"+str(current_level+1)
  levsurf,levRect=msg_text(lev,400,40)
  DISPLAYSURF.blit(levsurf,levRect)
def display_life(life,DISPLAYSURF):
  l="Attempts-"+str(life)
  lifesurf,lifeRect=msg_text(l,600,40)
  DISPLAYSURF.blit(lifesurf,lifeRect)

def display_screen(clock,player,event,DISPLAYSURF,target_object,infoSurf,infoRect,sourcex,target,fire_object):
  display_score(score,DISPLAYSURF)
  display_level(current_level,DISPLAYSURF)
  display_life(life,DISPLAYSURF)
  
  player.handle_event(event,current_level)
  DISPLAYSURF.blit(infoSurf, infoRect)

  
  


  
  

  DISPLAYSURF.blit(player.image, player.rect)
  
  
  
  
  for fire in fire_object:
    if fire.x!=sourcex:
      pygame.draw.circle(DISPLAYSURF, c.RED, (fire.x,fire.y), 8, 0)


  #pygame.draw.rect(DISPLAYSURF,target.color,(target.x,target.y,24,24))
  for target in target_object:
    DISPLAYSURF.blit(target.image, (target.xy[0],target.xy[1]+ 24))
    DISPLAYSURF.blit(target.surf, target.xy)

  
  clock.tick(c.tick[c.level[current_level]])
  pygame.display.update()
  #====================================================

def main_menu(DISPLAYSURF):
  global Game_start
  lev_delay=True
  while not Game_start:
    DISPLAYSURF.fill(c.BLACK)
    level_msg0="SDES Battle"
    level_msg1="Press Begin to Start"
    level_msg2="Begin"
    level_msg3=""        
    lifesurf0,lifeRect0=msg_text(level_msg0,screen_x/2,screen_y/2-100,c.BLUE,50)
    lifesurf1,lifeRect1=msg_text(level_msg1,screen_x/2,screen_y/2,c.BLUE,20)
    lifesurf2,lifeRect2=msg_text(level_msg2,screen_x/2,screen_y/2+50,c.GREEN,20)
    lifesurf3,lifeRect3=msg_text(level_msg3,screen_x/2,screen_y/2+80)
        
	    
    for event in pygame.event.get():
      if (event.type == pygame.MOUSEBUTTONDOWN):
	if(event.pos[0]>=screen_x/2 and event.pos[0]<=screen_x/2+35):
	  if(event.pos[1]>=screen_y/2+35 and event.pos[1]<=screen_y/2+50):
	    lifesurf2,lifeRect2=msg_text(level_msg2,screen_x/2,screen_y/2+60,c.GREEN)
	    Game_start=True
	  if(event.pos[1]>=screen_y/2+55 and event.pos[1]<=screen_y/2+70):
	    lifesurf3,lifeRect3=msg_text(level_msg3,screen_x/2,screen_y/2+80,c.GREEN)
	    #Game_start=True
      
      if event.type == QUIT:
	pygame.quit()
	sys.exit()
    
    DISPLAYSURF.blit(lifesurf0,lifeRect0)
    DISPLAYSURF.blit(lifesurf1,lifeRect1)
    DISPLAYSURF.blit(lifesurf2,lifeRect2)
    DISPLAYSURF.blit(lifesurf3,lifeRect3)
    pygame.display.flip()
    
  
  


def level_transition_func(DISPLAYSURF):
  global level_transition,Gameover
  lev_delay=True
  while level_transition:      
      while lev_delay:	
        DISPLAYSURF.fill(c.BLACK)
        level_msg0="Level:"+str(current_level+1)
        level_msg1="Do You Want To Continue ?"
        level_msg2="Yes"
        level_msg3="No"        
        lifesurf0,lifeRect0=msg_text(level_msg0,screen_x/2,screen_y/2+20)
        lifesurf1,lifeRect1=msg_text(level_msg1,screen_x/2,screen_y/2+40)
        lifesurf2,lifeRect2=msg_text(level_msg2,screen_x/2,screen_y/2+60)
        lifesurf3,lifeRect3=msg_text(level_msg3,screen_x/2,screen_y/2+80)
        
	    
        for event in pygame.event.get():
	  if (event.type == pygame.MOUSEBUTTONDOWN):
	    if(event.pos[0]>=screen_x/2 and event.pos[0]<=screen_x/2+35):
	      if(event.pos[1]>=screen_y/2+35 and event.pos[1]<=screen_y/2+50):
		lifesurf2,lifeRect2=msg_text(level_msg2,screen_x/2,screen_y/2+60,c.GREEN)
		lev_delay=False
	      if(event.pos[1]>=screen_y/2+55 and event.pos[1]<=screen_y/2+70):
		lifesurf3,lifeRect3=msg_text(level_msg3,screen_x/2,screen_y/2+80,c.GREEN)
		lev_delay=False
		Gameover=True
	 
	  if event.type == QUIT:
	    pygame.quit()
	    sys.exit()
	
	DISPLAYSURF.blit(lifesurf0,lifeRect0)
	DISPLAYSURF.blit(lifesurf1,lifeRect1)
	DISPLAYSURF.blit(lifesurf2,lifeRect2)
	DISPLAYSURF.blit(lifesurf3,lifeRect3)
        pygame.display.flip()
	
      
      level_transition=False
  
  #====================================================
def main():
  global score
  global Gameover
  global life

  global level_transition
  global screen_x
  global screen_y
  global e
  

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
  
  
  #counter_target_move = 0
  #counter_target_move = []
  target_object=[]
  #target_surf=[]
  #target_image=[]
  #target_xy=[]
  e=0
  #target_height=[]
  
  #====================================================
  target_object.append(make_target())
    #target_image.append(None)
    #target_object.append(0)
    #target_xy.append(0)
    #counter_target_move.append(0)
    #target_height.append (0)
  


  main_menu(DISPLAYSURF)
  #========================the main game loop========================
  while not Gameover:
    sourcex = player.rect[0]
    sourcey = player.rect[1]
    
    level_transition_func(DISPLAYSURF)

    
    #=======================Background Image=======================

    if current_level==background_counter:
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
    if (e < len(c.exam)):
      if random.randrange(0,200) in c.create_target:
	target_object.append(make_target())
      # target validity
    for target in target_object:
	target.move_target(target_object)
	
      
	# fire validity
    for fire in fire_object:	  
	if fire.valid:
	    fire.fire_now()
	if fire.x >= screen_x:
	      fire.destroy_fire(fire_object)
	      

	#   collision detection  
    for target in target_object:
      for fire in fire_object:
	    if fire.x < target.x+24 and fire.x > target.x and fire.y < target.y+target.height and fire.y > target.y:
	      fire.destroy_fire(fire_object)
	      target.surf,target.xy=msg_text('destroyed',target.x,target.y)
	      sound.destroy()
	      target_delay=c.delay[current_level]
	      score += target.score
	      target.destroy_target(target_object)
	      
	      
	      
	    
	      
	
	
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

      
	
    
    
    
    display_screen(clock,player,event,DISPLAYSURF,target_object,infoSurf,infoRect,sourcex,target,fire_object)
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
