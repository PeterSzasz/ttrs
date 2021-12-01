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
from game.states import GameState, Menu, Running, Scores

# game settings
GRID_WIDTH = 40
GRID_HEIGHT = 40
LEFT_BORDER = 7     # conclusive
RIGHT_BORDER = 15
MAP_WIDTH = RIGHT_BORDER - LEFT_BORDER

class GUI:
    def __init__(self, width, height) -> None:
        '''scene assets, settings, modes, etc'''

        self.state = Running()
        self.test_shape = 'L-shape'
        self.game_mode = "running"  # menu, running, paused, exit, scores
        self.width = width
        self.height = height        
        map_height = (height // GRID_HEIGHT)
        print(MAP_WIDTH)
        print(map_height)
        self.shapes = Shapes()
        self.playground = Map(MAP_WIDTH, map_height)
        self.player_pivot = (MAP_WIDTH//2,map_height-5)
        print(self.player_pivot)
        self.assets()
        self.draw_background()
        self.update_pivot()
        self.draw_playground()
    
    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def draw_background(self):
        col = 0
        row = 0
        # background
        for x in range(0, self.width, GRID_WIDTH):
            col += 1
            for y in range(0, self.height, GRID_HEIGHT):
                row += 1
                # a greyish belt in the background
                if 5<row and row<11:
                    self.image.blit_into(self.grey_box, x+1, y+1, 0)
                # black background
                else:
                    self.image.blit_into(self.black_box, x+1, y+1, 0)
            row = 0

    def draw_playground(self):
        col = LEFT_BORDER
        row = 0
        for x in range(LEFT_BORDER*GRID_WIDTH, RIGHT_BORDER*GRID_WIDTH, GRID_WIDTH):
            for y in range(0, self.height, GRID_HEIGHT):
                # middle green playground
                if LEFT_BORDER<=col and col<RIGHT_BORDER:
                    self.image.blit_into(self.green_box, x+1, y+1, 0)
                    # tetris tetriminos
                    scene_coords = (col-LEFT_BORDER, row)
                    grid_color = self.playground.check_grid(*scene_coords)
                    if grid_color is not None:
                        if grid_color == "blue":
                            self.image.blit_into(self.blue_box, x+1, y+1, 0)
                        if grid_color == "red":
                            self.image.blit_into(self.red_box, x+1, y+1, 0)
                        if grid_color == 'black':
                            self.image.blit_into(self.black_box, x+1, y+1, 0)
                row += 1
            col += 1
            row = 0

    def update_pivot(self, clear=False):
        #t_minos = self.shapes.tetriminos['L-shape']
        t_minos = self.shapes.tetriminos[self.test_shape]
        for box in t_minos['shape']:
            color = t_minos['color']
            x = self.player_pivot[0] + box[0]
            y = self.player_pivot[1] + box[1]
            print(x)
            print(y)
            if  0<=x and x<self.width and \
                0<=y and y<self.height:
                    if clear:
                        self.playground.color_grid(x,y,None)
                    else:
                        self.playground.color_grid(x,y,color)
       
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.state.on_key_press(key, modifiers)

    def draw(self):
        self.image.blit(0,0)
        self.label.draw()

    def assets(self):
        ## game assets, hidden at the end of class
        # background image, set in setup
        self.image = pyglet.image.SolidColorImagePattern((11,111,11,255)).create_image(self.width, self.height).get_texture()
        # texts, labels for scores and shirt
        self.label = pyglet.text.Label("Hello Tetris World!", x=20, y=self.height-25, font_size=15, color=(200,200,200,255),)
        #white_pixel = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(1,1)
        self.black_box = pyglet.image.SolidColorImagePattern((0,0,0,255)).create_image(GRID_WIDTH-1,GRID_HEIGHT-1)
        self.red_box = pyglet.image.SolidColorImagePattern((220,110,70,255)).create_image(GRID_WIDTH-1,GRID_HEIGHT-1)
        self.green_box = pyglet.image.SolidColorImagePattern((100,240,100,255)).create_image(GRID_WIDTH-1,GRID_HEIGHT-1)
        self.blue_box = pyglet.image.SolidColorImagePattern((110,150,220,255)).create_image(GRID_WIDTH-1,GRID_HEIGHT-1)
        self.grey_box = pyglet.image.SolidColorImagePattern((20,20,20,255)).create_image(GRID_WIDTH-1,GRID_HEIGHT-1)