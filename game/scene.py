##########################################
# class for game scene, everything that is in the window and interactive
# also handles game modes:
# "running" -> "scores" -esc-> "menu" -esc-> "exit?"
#   |-esc-> "menu"              |-enter-> "running"
# menu: up=speed-up down=speed-down esc=exit enter=game
# running: up,down,left,right=move-piece esc=menu p=paused
# exit?: enter=exit esc=menu
##########################################

import pyglet

from game.assets import Map, Shapes


class GUI:
    def __init__(self, width, height) -> None:
        '''scene assets, settings, modes, etc'''

        self.state = None
        self.width = width
        self.height = height
        self.grid_width = 40
        self.grid_height = 40
        
        # background image and building blocks
        self.image = pyglet.image.SolidColorImagePattern((11,111,11,255)).create_image(self.width, self.height).get_texture()
        self.white_pixel = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(2,2)
        self.black_box = pyglet.image.SolidColorImagePattern((0,0,0,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.grey_box = pyglet.image.SolidColorImagePattern((20,20,20,255)).create_image(self.grid_width-1,self.grid_height-1)

        self.draw_background()
        #self.update_pivot()
        #self.draw_playground()
    
    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def draw_background(self):
        #col = 0
        row = 0
        # background
        for x in range(0, self.width, self.grid_width):
            #col += 1
            for y in range(0, self.height, self.grid_height):
                row += 1
                # a greyish belt in the background
                if 5<row and row<11:
                    self.image.blit_into(self.grey_box, x+1, y+1, 0)
                # black background
                else:
                    self.image.blit_into(self.black_box, x+1, y+1, 0)
            row = 0

       
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.state:
            self.state.on_key_press(key, modifiers)

    def on_update(self, delta_time):
        if self.state:
            self.state.on_update(delta_time)

    def on_draw(self):
        self.image.blit(0,0)
        self.draw_background()
        if self.state:
            self.state.on_draw()
