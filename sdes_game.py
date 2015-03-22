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
  
def main():
  pygame.init()
  exam=['Assignment1','Assignment2','Midsem']
  FPS = 50 # frames per second setting
  fpsClock = pygame.time.Clock()

  # set up the window
  #DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
  DISPLAYSURF = pygame.display.set_mode((2000, 1000), 0, 32)

  pygame.display.set_caption('AE663 Pygame Project')

  

  #catImg = pygame.image.load('cat.png')
  sourcex = 10
  sourcey = 10

  clock=pygame.time.Clock()

  target = 'left'
  #targetx,targety=2000,40
  targetx,targety=2000,random.randrange(40,500)

  firex=sourcex
  firey=sourcey
  fire='stop'
  kill='missed'
  delay=0
  e=0
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
	target_surf,target_xy=msg_text(exam[e],targetx,targety)
	
	
	  
      if target=='right':
	targetx+=10
      
      if fire=='start':
	firex+=10
	if firex>2000:
	  #firex=sourcex
	  #firey=sourcey
	  fire='stop'
	  
      if kill=='killed':
	firey=sourcey
	firex=sourcex
	targetx,targety=2000,random.randrange(40,900)
	kill='missed'
	e=e+1
	
      
      r=20
      for i in range(r):
	t_x=targetx+i
	for j in range(r):
	  t_y=targety+j
	  if t_x==firex and t_y==firey:
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
	    fire='start'
	    firey=sourcey
	    firex=sourcex
	    
	    
	  #if event.key==pygame.K_LEFT:
	    #sourcex-=20
	  #if event.key==pygame.K_RIGHT:
	    #sourcex+=20
	  
	  if event.key==pygame.K_DOWN:
	    sourcey+=25
	    #firey=sourcey
	  if event.key==pygame.K_UP:
	    sourcey-=25
	    #firey=sourcey
	  
    DISPLAYSURF.blit(target_surf, target_xy)
    DISPLAYSURF.blit(infoSurf, infoRect)
    #DISPLAYSURF.blit(catImg, (0, 0))
    #pygame.draw.circle(surface, color, center_point, radius, width)

    pygame.draw.circle(DISPLAYSURF, RED, (firex,firey), 10, 0)

    pygame.draw.rect(DISPLAYSURF,BLUE,(targetx,targety,20,20))
    
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