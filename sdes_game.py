import pygame, sys
import random
from pygame.locals import *

WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)

color=[DARKGRAY,BLACK,BRIGHTRED,RED,BRIGHTGREEN,GREEN,BRIGHTBLUE,BRIGHTYELLOW]
class make_fire(object):
  def __init__(self,x,y,sourcex,sourcey,fire):
      self.x, self.y = sourcex,sourcey+20
      self.fire=fire
  def fire_load(self):
      return self.x,self.y
  
  def fire_now(self):
    if self.fire=='start':
      self.x+=10
      if self.x>2000:
	#firex=sourcex
	#firey=sourcey
	self.fire='stop'
      return self.x,self.y,self.fire
    
    
def main():
  pygame.init()
  exam=['Assignment1','Assignment2','Quiz1','Assignment3','Midsem','Assignment4','Quiz2','end-sem']
  FPS = 50 # frames per second setting
  fpsClock = pygame.time.Clock()

  # set up the window
  #DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
  DISPLAYSURF = pygame.display.set_mode((2000, 1000), 0, 32)

  pygame.display.set_caption('AE663 Pygame Project')

  

  #catImg = pygame.image.load('turtle_as_player.png')
  sourcex = 10
  sourcey = 10
  no_of_fire=100
  fire=[]
  fire_object=[]
  firex=[]
  firey=[]
  valid_fire=[]
  
  clock=pygame.time.Clock()

  target = 'left'
  #targetx,targety=2000,40
  targetx,targety=2000,random.randrange(40,500)
  
  for i in range(no_of_fire):
    fire.append('stop')
    fire_obj=make_fire(0,0,sourcex,sourcey,fire[i])
    fire_object.append(fire_obj)
    f_x,f_y=fire_object[i].fire_load()
    firex.append(f_x)
    firey.append(f_y)
    valid_fire.append(0)
  
  kill='missed'
  delay=0
  e=0
  f=0
  c=0
  while True: # the main game loop
      
    DISPLAYSURF.fill(WHITE)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BASICFONT.render('AE663 Pygame Project', 1, DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, 1000 - 25)
    #catImg=pygame.transform.rotate(catImg,90)
    #to rotate image by 90 degree
    if delay>0:
      delay=delay-1
    else:      
      if target=='left':
	targetx-=5
	if targetx<0:
	  targetx,targety=2000,random.randrange(40,900)
	  e=e+1
	  if e>len(exam)-1:
	   e=0
	  c=random.randrange(0,len(color))
	target_surf,target_xy=msg_text(exam[e],targetx,targety)
	
	
	  
      if target=='right':
	targetx+=10
      
      #if fire=='start':
	#firex+=10
	#if firex>2000:
	  ##firex=sourcex
	  ##firey=sourcey
	  #fire='stop'
      for i in range(no_of_fire):
	if valid_fire[i]==1:
	  firex[i],firey[i],fire[i]=fire_object[i].fire_now()
	if fire[i]=='stop':
	  valid_fire[i]=0
      
      
      if kill=='killed':
	valid_fire[destroy_fire]=0
	firey[destroy_fire]=sourcey+20
	firex[destroy_fire]=sourcex
	targetx,targety=2000,random.randrange(40,900)
	kill='missed'
	e=e+1
	if e>len(exam)-1:
	  e=0
	c=random.randrange(0,len(color))
	
	
      
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
		kill='killed'
		r=0
		delay=15
	  
	
	      
      for event in pygame.event.get():
	if event.type == QUIT:
	  pygame.quit()
	  sys.exit()
	  
	if event.type==pygame.KEYDOWN:
	  if event.key==pygame.K_f:
	    valid_fire[f]=1
	    fire[f]='start'
	    fire_object[f]=make_fire(0,0,sourcex,sourcey,fire[f])
	    firex[f],firey[f]=fire_object[f].fire_load()
	    f=f+1
	    if f>no_of_fire-1:
	      f=0
	    
	    
	  #if event.key==pygame.K_LEFT:
	    #sourcex-=20
	  #if event.key==pygame.K_RIGHT:
	    #sourcex+=20
	  
	  if event.key==pygame.K_DOWN:
	    sourcey+=24
	    if sourcey>940:
	      sourcey=940
	    #firey=sourcey
	  if event.key==pygame.K_UP:
	    sourcey-=24
	    if sourcey<10:
	      sourcey=10
	    #firey=sourcey
	  
    DISPLAYSURF.blit(target_surf, target_xy)
    DISPLAYSURF.blit(infoSurf, infoRect)
    #DISPLAYSURF.blit(catImg, (20,40))
    #pygame.draw.circle(surface, color, center_point, radius, width)
    for j in range(no_of_fire):
      if firex[j]!=sourcex:
	pygame.draw.circle(DISPLAYSURF, RED, (firex[j],firey[j]), 8, 0)

    pygame.draw.rect(DISPLAYSURF,color[c],(targetx,targety,24,24))
      
    pygame.draw.rect(DISPLAYSURF,BLACK,(sourcex,sourcey,20,40))
    
    clock.tick(40)
    
    pygame.display.update()
    
    fpsClock.tick(FPS)
    
#def msg_text(text,textcolor):
  #smalltext=pygame.font.Font('freesansbold.ttf',20)
  #largetext=pygame.font.Font('freesansbold.ttf',150)
  
  #titletextsurf,titletextrect=msg_text)

def msg_text(text,x,y):  
 FONT = pygame.font.Font('freesansbold.ttf', 16)
 Surf = FONT.render(text, 1, DARKGRAY)
 Rect = Surf.get_rect()
 Rect.topleft = (x, y - 25) 
 return Surf,Rect

main()
