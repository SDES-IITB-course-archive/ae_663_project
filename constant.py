
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

#terminal name
terminal_name='AE663 Pygame Project'

#target colors
color=[DARKGRAY,BLACK,BRIGHTRED,RED,BRIGHTGREEN,GREEN,BRIGHTBLUE,BRIGHTYELLOW]
#target_image_list = ["target_turtle.png", "goomba.png", "target_turtle.png", "goomba.png", "target_turtle.png", "target_turtle.png", "target_turtle.png", "target_turtle.png"]
#target names
#exam=['dummy','Assignment1']
exam=['Assignment1','Assignment2','Quiz1','Assignment3','Midsem','Assignment4','Quiz2','end-sem']
score = [2,3,5,2,8,3,5,12]
passingmark=1

enemy_image_1 = [ "target_images/bluemonster1.png", "target_images/bowser-fireball1.png", "target_images/monster-red1.png", "target_images/slub1.png", "target_images/squidge1.png", "target_images/slubblue1.png", "target_images/spiker1.png", "target_images/bowser1.png"]
enemy_image_2 = [ "target_images/bluemonster2.png", "target_images/bowser-fireball2.png", "target_images/monster-red2.png", "target_images/slub2.png", "target_images/squidge2.png", "target_images/slubblue2.png", "target_images/spiker2.png", "target_images/bowser2.png"]

#fire states
stop='stop'
start='start'

#target states
left='left'

#collision states
killed='killed'
missed='missed'

#clock tick
tick=[30,50,100]

#levels
level=[0,1,2]
level_delay=600

#delay between targets
delay=[10,5,0]
level_delay=600

#player step
player_step=[5,5,5]



# Background Image
image_name =["background_images/cartoon.jpg","background_images/image_sea.jpg","background_images/sulfuronspire.jpg"]
#Speed at which background is moving
background_speed = [0.5, 0.6, 0.7]


#Fire position adjustment
fire_starting_shift_x= 50
fire_starting_shift_y= 50


#Target height to be shot
target_width = 150
target_height = 100

#create_target
create_target = [99]