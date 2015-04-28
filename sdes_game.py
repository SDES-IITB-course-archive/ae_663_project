import pygame
from Xlib import display
import random
from pygame.locals import *
from pygame.transform import scale
import serge
import constant as c


#============Global Variables========================

score = 0
current_level=0 # define global in the functions where you want to update this variable
level_transition=False
life = 3
Gameover=False
Game_start=False
exam_counter=0
level_score=[]
pause=False
stat_color=c.WHITE
#====================================================

def reset():
  global score,current_level,level_transition,life,Gameover,Game_start,exam_counter,level_score,pause  
  score = 0
  current_level=0 # define global in the functions where you want to update this variable
  level_transition=False
  life = 3
  Gameover=False
  Game_start=False
  exam_counter=0
  level_score=[]
  pause=False


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
    global current_level,level_transition,exam_counter,life
    self.x, self.y = screen_x,random.randrange(40,screen_y-100)
    self.valid = True
    self.score = c.score[exam_counter]
    self.image1 = c.enemy_image_1[exam_counter]
    self.image2 = c.enemy_image_2[exam_counter]
    self.image = pygame.image.load(self.image1).convert()
    self.image = pygame.transform.scale2x(self.image)
    self.surf,self.xy=msg_text(c.exam[exam_counter],self.x, self.y)
    self.image_counter = 0
    self.height = self.image.get_height()
    self.e1 = exam_counter
    exam_counter += 1

  def move_target(self,target_object):
    global current_level,level_transition,exam_counter,life
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
    global current_level,level_transition,exam_counter,Gameover
    target_object.remove(self)
    print exam_counter, len(c.exam) , len(target_object)
    if(exam_counter == len(c.exam) and len(target_object) == 0):
      if current_level < 2:
	if current_level>0:
	  print "curr",current_level,"  score-",score,"  level_score-",level_score
	  level_score.append(score-level_score[current_level-1])
	else:
	  level_score.append(score)
	
	current_level += 1
	level_transition = True
	exam_counter = 0
      else:
	Gameover = True
    
    
  #====================================================

def get_resolution():
  resolution = display.Display().screen().root.get_geometry()
  return resolution.width, resolution.height

  #====================================================

  #====================================================
def display_score(score, DISPLAYSURF):
  s="Marks-"+str(score)
  scoresurf,scoreRect=msg_text(s,800,40,stat_color)
  DISPLAYSURF.blit(scoresurf, scoreRect)
  
def display_level(current_level,DISPLAYSURF):
  lev="Level-"+str(current_level+1)
  levsurf,levRect=msg_text(lev,400,40,stat_color)
  DISPLAYSURF.blit(levsurf,levRect)
  
def display_life(life,DISPLAYSURF):
  l="Attempts-"+str(life)
  lifesurf,lifeRect=msg_text(l,600,40,stat_color)
  DISPLAYSURF.blit(lifesurf,lifeRect)

def display_info(DISPLAYSURF,screen_x):
  l="p:pause  f:fire"
  print "screen_y",screen_y
  helpsurf,helpRect=msg_text(l,screen_x-250,30,stat_color)
  DISPLAYSURF.blit(helpsurf,helpRect)
  
def display_pause(pause_msg,DISPLAYSURF):
  pausesurf,pauseRect=msg_text(pause_msg,screen_x/2,screen_y/2+60)
  DISPLAYSURF.blit(pausesurf,pauseRect)


def display_screen(clock,player,screen_y,screen_x,event,DISPLAYSURF,target_object,infoSurf,infoRect,fire_object):
  DISPLAYSURF.blit(infoSurf, infoRect) 
  display_score(score,DISPLAYSURF)
  display_level(current_level,DISPLAYSURF)
  display_life(life,DISPLAYSURF)
  display_info(DISPLAYSURF,screen_x)
  
  player.handle_event(event,current_level,screen_y)
  DISPLAYSURF.blit(player.image, player.rect)
  for fire in fire_object:
    pygame.draw.circle(DISPLAYSURF, c.RED, (fire.x,fire.y), 8, 0)
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
    lifesurf0,lifeRect0=msg_text(level_msg0,screen_x/2-400,screen_y/2-250,c.BLUE,150)
    lifesurf1,lifeRect1=msg_text(level_msg1,screen_x/2-250,screen_y/2-60,c.BLUE,60)
    lifesurf2,lifeRect2=msg_text(level_msg2,screen_x/2-20,screen_y/2+50,c.GREEN,30)
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
  global level_transition,Gameover,current_level,stat_color
  lev_delay=True
  while level_transition:
      while lev_delay:
        DISPLAYSURF.fill(c.BLACK)
	if score>20:
	  level_msg0="Level:"+str(current_level+1)
	  level_msg1="Do You Want To Continue ?"
	  level_msg2="Yes"
	  level_msg3="No"
	  s0=80
	  l0=200
	else:
	  level_msg0="Marks Less Than 'Passing Marks'"
	  level_msg1="Do You Want To Retry ?"
	  level_msg2="Yes"
	  level_msg3="No"
	  s0=60
	  l0=400
        lifesurf0,lifeRect0=msg_text(level_msg0,screen_x/2-l0,screen_y/2-200,c.WHITE,s0)
        lifesurf1,lifeRect1=msg_text(level_msg1,screen_x/2-400,screen_y/2-100,c.WHITE,60)
        lifesurf2,lifeRect2=msg_text(level_msg2,screen_x/2-100,screen_y/2,c.WHITE,40)
        lifesurf3,lifeRect3=msg_text(level_msg3,screen_x/2-100,screen_y/2+50,c.WHITE,40)
        
	    
        for event in pygame.event.get():
	  if (event.type == pygame.MOUSEBUTTONDOWN):
	    if(event.pos[0]>=screen_x/2-100 and event.pos[0]<=screen_x/2):
	      if(event.pos[1]>=screen_y/2-60 and event.pos[1]<=screen_y/2):
		lifesurf2,lifeRect2=msg_text(level_msg2,screen_x/2-100,screen_y/2,c.GREEN,30)
		lev_delay=False
		if s0==60:
		  reset()
		  main()
	      if(event.pos[1]>=screen_y/2+40 and event.pos[1]<=screen_y/2+100):
		lifesurf3,lifeRect3=msg_text(level_msg3,screen_x/2-100,screen_y/2+50,c.GREEN,30)
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
	
      if((current_level+1)%2==0): stat_color=c.BLACK
      else: stat_color=c.WHITE
      level_transition=False
def update_target(target_object):
  global exam_counter, marker,create_target
  for target in target_object:
	target.move_target(target_object)
  if (exam_counter < len(c.exam)):
      if random.randrange(0,200) in create_target and len(target_object) < 4 and marker > 30:
	target_object.append(make_target())
	marker = 0
      else:
	marker +=1

def update_fire(fire_object):
  for fire in fire_object:	  
	if fire.valid:
	    fire.fire_now()
	    if fire.x >= screen_x:
	      fire.destroy_fire(fire_object)

def collision_detection(fire_object,target_object,sound):	
    global score
    for target in target_object:
      for fire in fire_object:
	    if fire.x < target.x+24 and fire.x > target.x and fire.y < target.y+target.height and fire.y > target.y:
	      fire.destroy_fire(fire_object)
	      target.surf,target.xy=msg_text('destroyed',target.x,target.y)
	      sound.destroy()
	      target_delay=c.delay[current_level]
	      score += target.score
	      target.destroy_target(target_object)
	
def refresh_background(DISPLAYSURF,fire_object):
   global score,current_level,create_target,background_counter,x_back_ground_start,y_back_ground_start,background_image
   if current_level==background_counter:
      score = 0
      create_target.append(random.randrange(0,200))
      print "create_target[]-",create_target
      fire_object=[]
      background_counter=(background_counter+1)
      background_image = pygame.image.load(c.image_name[current_level]).convert()
      x_back_ground_start=0
      y_back_ground_start=0
      print x_back_ground_start,c.background_speed [current_level]
      #DISPLAYSURF=background_image_set (DISPLAYSURF, background_image,[x_back_ground_start,y_back_ground_start])
      if background_counter==len(c.level):
	background_counter=0
    
    #===============Moving the Background===========================
   x_back_ground_start = x_back_ground_start - c.background_speed [current_level]
   DISPLAYSURF=background_image_set(DISPLAYSURF, background_image, [x_back_ground_start, y_back_ground_start])
#====================================================


def pause_state(DISPLAYSURF):
  global pause
  count=0
  while(pause):
    pause_msg="Pause"
    for event in pygame.event.get():
      if event.type == QUIT:
	pygame.quit()
	sys.exit()
      if event.type==pygame.KEYDOWN:
	if event.key==pygame.K_p:
	  pause=False
	  count=100
	  pause_msg="Play"
    
    display_pause(pause_msg,DISPLAYSURF)
    pygame.display.update()
  while(count>0): 
    count-=1
    display_pause(pause_msg,DISPLAYSURF)
    pygame.display.update()
#====================================================
	    
  
def main():
  global score,Gameover,life,level_transition,screen_x,screen_y,exam_counter,pause,marker,create_target,background_counter

  sound = audio()
  screen_x, screen_y = get_resolution()
  #================define terminal size================
  DISPLAYSURF = display_init()
  
  #================define Local Variables================

  marker = 0
  sourcex,sourcey = 10,10
  fire_object=[]
  target_object=[]
  player = serge.Serge((sourcex, sourcey))
  clock=pygame.time.Clock()
  target_delay=0
  x_back_ground_start=0
 
  background_counter=0
  exam_counter=0
  create_target=[]
  #====================================================
  target_object.append(make_target())
    #target_image.append(None)
    #target_object.append(0)
    #target_xy.append(0)
    #counter_target_move.append(0)
    #target_height.append (0)
  infoSurf,infoRect=msg_text(c.terminal_name,10,screen_x)


  main_menu(DISPLAYSURF)
  #========================the main game loop========================
  while not Gameover:
    sourcex,sourcey = player.rect[0],player.rect[1]
    level_transition_func(DISPLAYSURF)
  
    #=======================Background Image=======================

    refresh_background(DISPLAYSURF,fire_object)
    
   
   #================================================================
    
    
   
      # target validity
    update_target(target_object)
    update_fire(fire_object)
    collision_detection(fire_object,target_object,sound)	 

    for event in pygame.event.get():
	  if event.type == QUIT:
	    pygame.quit()
	    #sys.exit()
	  if event.type==pygame.KEYDOWN:
	    if event.key==pygame.K_f:
	      fire_object.append(make_fire(sourcex,sourcey))
	      sound.fire()
	    if event.key==pygame.K_p:
	       pause=True  
	    if event.key==pygame.K_DOWN:
	      sourcey+=24
	      if sourcey>screen_y-50:
		sourcey=screen_y-50
	    if event.key==pygame.K_UP:
	      sourcey-=24
	      if sourcey<10:
		sourcey=10

      
    pause_state(DISPLAYSURF)   
    

    display_screen(clock,player,screen_y,screen_x,event,DISPLAYSURF,target_object,infoSurf,infoRect,fire_object)

  #==================================================================
  
  while Gameover:
    DISPLAYSURF.fill(c.BLACK)
    lifesurf,lifeRect=msg_text("Game Over",screen_x/2-300,screen_y/2,c.WHITE,80)
    
    
    DISPLAYSURF.blit(lifesurf,lifeRect)
    pygame.display.flip()
    
    for event in pygame.event.get():
	if event.type == QUIT:
	  pygame.quit()
	  #sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            #Gameover = False
	  
    

main()
