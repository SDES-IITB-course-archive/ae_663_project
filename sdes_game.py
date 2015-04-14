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

  #====================================================
def create_fires(sourcex,sourcey,fire_object,firex,firey,valid_fire,no_of_fire,screen_x):
  for i in range(no_of_fire):
    valid_fire.append(0)
    fire_obj=make_fire(0,0,sourcex,sourcey,valid_fire[i],screen_x)
    fire_object.append(fire_obj)
    f_x,f_y=fire_object[i].fire_load()
    firex.append(f_x)
    firey.append(f_y)
  #====================================================

  #====================================================
class make_fire(object):
  def __init__(self,x,y,sourcex,sourcey,valid_fire,screen_x):
      self.x, self.y = sourcex,sourcey+20
      self.valid_fire=valid_fire
      self.screen_x=screen_x
  
  def fire_load(self):
      return self.x,self.y
  
  def fire_now(self):
    if self.valid_fire==1:
      self.x+=10
      if self.x>self.screen_x:
	self.valid_fire=0
      return self.x,self.y,self.valid_fire
  #====================================================

  #====================================================
def display_screen(clock,current_level,player,event,color_counter,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,no_of_fire,sourcex,firex,firey,targetx,targety):
  player.handle_event(event)
  DISPLAYSURF.blit(target_surf, target_xy)
  DISPLAYSURF.blit(infoSurf, infoRect)
  #DISPLAYSURF.blit(image, (20,40))
  #DISPLAYSURF.blit(image, (sourcex,sourcey))
  DISPLAYSURF.blit(player.image, player.rect)

  #pygame.draw.circle(surface, color, center_point, radius, width)
  for j in range(no_of_fire):
    if firex[j]!=sourcex:
      pygame.draw.circle(DISPLAYSURF, c.RED, (firex[j],firey[j]), 8, 0)

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
  
  
  sourcex = 10
  sourcey = 10
  no_of_fire=100
  fire_object=[]
  firex=[]
  firey=[]
  valid_fire=[]
  player = serge.Serge((sourcex, sourcey))
  clock=pygame.time.Clock()
  target = c.left
  targetx,targety=screen_x,random.randrange(40,screen_y-100)
  create_fires(sourcex,sourcey,fire_object,firex,firey,valid_fire,no_of_fire,screen_x)
  kill=c.missed
  e=0
  f=0
  color_counter=0
  current_level=0
  target_delay=0
  
  #========================the main game loop========================
  while True:
    sourcex = player.rect[0]
    sourcey = player.rect[1]
    #===============Reload the display===============
    DISPLAYSURF.fill(c.WHITE)
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
     
      for i in range(no_of_fire):
	if valid_fire[i]==1:
	  firex[i],firey[i],valid_fire[i]=fire_object[i].fire_now()
	
      
      if kill==c.killed:
	valid_fire[destroy_fire]=0
	firey[destroy_fire]=sourcey+20
	firex[destroy_fire]=sourcex
	targetx,targety=screen_x,random.randrange(40,screen_y-100)
	kill=c.missed
	e=e+1
	if e>len(c.exam)-1:
	  e=0
	  current_level=current_level+1
	  if current_level>len(c.level)-1:
	   current_level=0
	color_counter=random.randrange(0,len(c.color))
	
	
      r=24
      destroy_fire=-1
      for i in range(r):
	t_x=targetx+i
	for j in range(r):
	  t_y=targety+j
	  for k in range(no_of_fire):
	    if valid_fire[k]==1:
	      if t_x==firex[k] and t_y==firey[k]:
		destroy_fire=k
		target_surf,target_xy=msg_text('destroyed',targetx,targety)
		kill=c.killed
		r=0
		target_delay=c.delay[current_level]
	  
	
	      
      for event in pygame.event.get():
	if event.type == QUIT:
	  pygame.quit()
	  sys.exit()
	  
	if event.type==pygame.KEYDOWN:
	  if event.key==pygame.K_f:
	    valid_fire[f]=1
	    fire_object[f]=make_fire(0,0,sourcex,sourcey,valid_fire[f],screen_x)
	    firex[f],firey[f]=fire_object[f].fire_load()
	    f=f+1
	    if f>no_of_fire-1:
	      f=0
	    
	  	  
	  if event.key==pygame.K_DOWN:
	    sourcey+=24
	    if sourcey>screen_y-50:
	      sourcey=screen_y-50
	  if event.key==pygame.K_UP:
	    sourcey-=24
	    if sourcey<10:
	      sourcey=10
	  
    display_screen(clock,current_level,player,event,color_counter,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,no_of_fire,sourcex,firex,firey,targetx,targety)
  #==================================================================
    



main(2000,1000)
