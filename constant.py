
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
target_image_list = ["target_turtle.png", "goomba.png", "target_turtle.png", "goomba.png", "target_turtle.png", "target_turtle.png", "target_turtle.png", "target_turtle.png"]
#target names
exam=['Assignment1','Assignment2','Quiz1','Assignment3','Midsem','Assignment4','Quiz2','end-sem']

#fire states
stop='stop'
start='start'

#target states
left='left'

#collision states
killed='killed'
missed='missed'

#clock tick
tick=[20,50,100]

#levels
level=[0,1,2]

#delay between targets
delay=[10,5,0]

#player step
player_step=[10,5,2]



# Background Image
image_name ="cartoon.jpg"
#Speed at which background is moving
background_speed = [0.5, 1, 2]


#Fire position adjustment
fire_starting_shift_x= 50
fire_starting_shift_y= 50


#Target height to be shot
target_width = 150
target_height = 100