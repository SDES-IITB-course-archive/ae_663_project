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


<<<<<<< HEAD
# do something
  #====================================================
=======


#====================================================

>>>>>>> 42463a0812abcdd139b8cfeda9b90705fc322886
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
<<<<<<< HEAD
def get_resolution():
  resolution = display.Display().screen().root.get_geometry()
  return resolution.width, resolution.height
  
def display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object):
=======

#def display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object):
  #====================================================

def display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object,target_image):
>>>>>>> 42463a0812abcdd139b8cfeda9b90705fc322886
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
  
  
  
  
  
  
  
  for j in range(len(fire_object)):
    if fire_object[j].x!=sourcex:
      pygame.draw.circle(DISPLAYSURF, c.RED, (fire_object[j].x,fire_object[j].y), 8, 0)


  #pygame.draw.rect(DISPLAYSURF,target.color,(target.x,target.y,24,24))
  for i in range(len(target)):
    DISPLAYSURF.blit(target_image [i], (target_xy [i] [0],target_xy [i] [1]+ 24))
    DISPLAYSURF.blit(target_surf[i], target_xy[i])

  
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
<<<<<<< HEAD
  sound = audio()
  screen_x, screen_y = get_resolution()
=======
  global e
  resolution = display.Display().screen().root.get_geometry()
  screen_x, screen_y = resolution.width, resolution.height
  print screen_x, screen_y
  
  screen_x, screen_y = resolution.width, resolution.height

>>>>>>> 42463a0812abcdd139b8cfeda9b90705fc322886
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
  counter_target_move = []
  target=[]
  target_surf=[]
  target_image=[]
  target_xy=[]
  e=0
  target_height=[]
  
  #====================================================
  for t in range(random.randrange(2,4)):
    target.append(Enemy())
    target_image.append(None)
    target_surf.append(0)
    target_xy.append(0)
    counter_target_move.append(0)
    target_height.append (0)
  


  main_menu(DISPLAYSURF)
  #========================the main game loop========================
  while not Gameover:
    sourcex = player.rect[0]
    sourcey = player.rect[1]
    
    level_transition_func(DISPLAYSURF)

    
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
#<<<<<<< HEAD
	#target_surf[tar],target_xy[tar]=msg_text(c.exam[target[tar].ee],target[tar].x,target[tar].y)
	
	


	#for fire in fire_object:
	  #if fire.valid:
	    #fire.fire_now()
	    #if fire.x < target[tar].x+24 and fire.x > target[tar].x and fire.y < target[tar].y+24 and fire.y > target[tar].y:
	      #fire.destroy_fire(fire_object)
	      #target_surf[tar],target_xy[tar]=msg_text('destroyed',target[tar].x,target[tar].y)
	      #target_delay=c.delay[current_level]
	      #target[tar].make_target()
	      #score+= target[tar].score
#=======
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
	target_image [tar] = pygame.transform.scale2x(target_image [tar])
	target_height[tar] = target_image [tar].get_height();
	#DISPLAYSURF.blit(target_image, (targetx,targety))
      
	

	for fire in fire_object:
<<<<<<< HEAD
	  if fire.valid:
	    fire.fire_now()
	    if fire.x < target[tar].x+24 and fire.x > target[tar].x and fire.y < target[tar].y+24 and fire.y > target[tar].y:
	      fire.destroy_fire(fire_object)
	      target_surf[tar],target_xy[tar]=msg_text('destroyed',target[tar].x,target[tar].y)
	      sound.destroy()
	      target_delay=c.delay[current_level]
	      target[tar].make_target()
	      score+= target[tar].score
=======
	    if fire.valid:
	      fire.fire_now()
	      if fire.x < target[tar].x+24 and fire.x > target[tar].x and fire.y < target[tar].y+ target_height[tar] and fire.y > target[tar].y:
		fire.destroy_fire(fire_object)
		target_surf[tar],target_xy[tar]=msg_text('destroyed',target[tar].x,target[tar].y)
		target_delay=c.delay[current_level]
		target[tar].make_target()
		score+= target[tar].score
#>>>>>>> fe3e7fe06861b0cecc0d59a972b772f707d008aa
>>>>>>> 42463a0812abcdd139b8cfeda9b90705fc322886
	      
	      
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
#<<<<<<< HEAD
  
    
    #display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object)

#=======
      
	target_image [tar].set_colorkey(c.BLACK)
    
    
    
    display_screen(clock,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object, target_image)
#>>>>>>> fe3e7fe06861b0cecc0d59a972b772f707d008aa
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
