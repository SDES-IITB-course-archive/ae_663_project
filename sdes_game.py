import pygame, sys
import random
from pygame.locals import *
from pygame.transform import scale
import math,subprocess
import os
import serge
import constant as c

  #====================================================
def display_init(screen_x,screen_y):
  pygame.init()
  DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)
  pygame.display.set_caption(c.terminal_name)
  return DISPLAYSURF
  #====================================================
  
  #====================================================
def msg_text(text,x,y):  
 FONT = pygame.font.Font('freesansbold.ttf', 16)
 Surf = FONT.render(text, 1, c.DARKGRAY)
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
  def __init__(self,sourcex,sourcey,screen_x):
      self.x, self.y = sourcex + c.fire_starting_shift_x, sourcey + c.fire_starting_shift_y
      self.valid=True
      self.screen_x=screen_x
  
  def fire_load(self):
      return self.x,self.y
  
  def fire_now(self):
    if self.valid:
      self.x+=5
      
  def destroy_fire(self,k,fire_object):
    fire_object.pop(k)
      
  #====================================================

  #====================================================
def display_screen(clock,current_level,player,event,color_counter,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,targetx,targety,fire_object):
  player.handle_event(event,current_level)
  DISPLAYSURF.blit(target_surf, target_xy)
  DISPLAYSURF.blit(infoSurf, infoRect)
  #DISPLAYSURF.blit(image, (20,40))
  #DISPLAYSURF.blit(image, (sourcex,sourcey))
  DISPLAYSURF.blit(player.image, player.rect)

  #pygame.draw.circle(surface, color, center_point, radius, width)
  for j in range(len(fire_object)):
    if fire_object[j].x!=sourcex:
      pygame.draw.circle(DISPLAYSURF, c.RED, (fire_object[j].x,fire_object[j].y), 8, 0)

  pygame.draw.rect(DISPLAYSURF,c.color[color_counter],(targetx,targety,24,24))
  #pygame.draw.rect(DISPLAYSURF,BLACK,(sourcex,sourcey,20,40))
  clock.tick(c.tick[c.level[current_level]])
  pygame.display.update()
  #====================================================
  
  #====================================================
def main(screen_x,screen_y):
  
  #================define terminal size================
  DISPLAYSURF = display_init(screen_x,screen_y)
  #====================================================
  
  
  #===============define background image===============
  #catImg = pygame.image.load('mario.png')
  #====================================================
  
  destroy = []
  sourcex = 10
  sourcey = 10
  no_of_fire=100
  fire_object=[]
  player = serge.Serge((sourcex, sourcey))
  clock=pygame.time.Clock()
  target = c.left
  targetx,targety=screen_x,random.randrange(40,screen_y-100)
  kill=c.missed
  e=0
  f=0
  color_counter=0
  current_level=0
  target_delay=0
  
  x_back_ground_start=0
  y_back_ground_start=0
  
 #=======================Background Image=======================
  #background_image_set ("desert.png")
  background_image = pygame.image.load(c.image_name).convert()
  DISPLAYSURF=background_image_set (DISPLAYSURF, background_image,[x_back_ground_start,y_back_ground_start])

  
  
  #========================the main game loop========================
  while True:
    sourcex = player.rect[0]
    sourcey = player.rect[1]
    
    
    
    
    #===============Moving the display===============
    x_back_ground_start = x_back_ground_start - c.background_speed [current_level]
    DISPLAYSURF=background_image_set (DISPLAYSURF, background_image, [x_back_ground_start, y_back_ground_start])
    
   
   #================================================
    
    infoSurf,infoRect=msg_text(c.terminal_name,10,screen_y)
    
    if target_delay>0:
      target_delay=target_delay-1
    else:
      if target==c.left:
	targetx-=5
	if targetx<0:
	  targetx,targety=screen_x,random.randrange(40,screen_y-100)
	  e=e+1
	  if e>len(c.exam)-1:
	   e=0
	   current_level=current_level+1
	   if current_level>len(c.level)-1:
	     current_level=0
	  color_counter=random.randrange(0,len(c.color))
	target_surf,target_xy=msg_text(c.exam[e],targetx,targety)
     
      for i in range(len(fire_object)):
	if fire_object[i].valid:
	  fire_object[i].fire_now()
	
      
      
	
	
	
	
      destroy = []
      for k in range(len(fire_object)):
	if fire_object[k].valid:
	  if fire_object[k].x < targetx+24 and fire_object[k].x > targetx and fire_object[k].y < targety+24 and fire_object[k].y > targety:
	    fire_object[k].valid = False
	    destroy.append(k)
	    target_surf,target_xy=msg_text('destroyed',targetx,targety)
	    targetx,targety=screen_x,random.randrange(40,screen_y-100)
	    target_delay=c.delay[current_level]
	    e=e+1
	    if e>len(c.exam)-1:
	      e=0
	      current_level=current_level+1
	      if current_level>len(c.level)-1:
		current_level=0
	    color_counter=random.randrange(0,len(c.color))
	  if fire_object[k].x >= screen_x:
	    fire_object[k].valid = False
	    destroy.append(k)
      i=0
      for k in destroy:
	#print destroy
	#print k,fire_object[k-i]
	fire_object[k-i].destroy_fire(k-i,fire_object)
	i+=1
      for event in pygame.event.get():
	if event.type == QUIT:
	  pygame.quit()
	  sys.exit()
	  
	if event.type==pygame.KEYDOWN:
	  if event.key==pygame.K_f:
	    fire_object.append(make_fire(sourcex,sourcey,screen_x))
	    
	    
	    
	  	  
	  if event.key==pygame.K_DOWN:
	    sourcey+=24
	    if sourcey>screen_y-50:
	      sourcey=screen_y-50
	  if event.key==pygame.K_UP:
	    sourcey-=24
	    if sourcey<10:
	      sourcey=10
	  
    display_screen(clock,current_level,player,event,color_counter,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,targetx,targety,fire_object)
  #==================================================================
    



main(1200,700)