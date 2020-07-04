# Imagine you are creating a Super Mario game.
#  You need to define a class to represent Mario. What would it look like?
#   If you aren't familiar with SuperMario, use your own favorite video or board game to model a player. 

class Mario:
    mario_img_walk = image_1
    mario_img_left = image_2
    mario_img_top = image_3
    mario_img_on_air = image_4
    

    def __init__(self):
        self.in_air = False
        self.walk = True
        self.mario_current_img = mario_img_walk

    def on_air(self):
       self.in_air = True
       self.walk = False
       self.mario_current_img = mario_img_on_air

    def walk(self):
        self.in_air = False
        self.walk = True


    def gobackward(self):
        self.mario_init_img = self.mario_img_left
