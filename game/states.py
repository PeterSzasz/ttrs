
# state pattern classes; GameState base class for Menu,Scores,etc
# context is the GUI class

from time import time
from pyglet import window
from pyglet.app import exit
from pyglet.text import Label
from pyglet.image import SolidColorImagePattern
from game.assets import Map, Shapes

class GameState:
    def __init__(self) -> None:
        ''''''
        pass

    def on_key_press(self, key, modifiers):
        ''''''
        pass

    def on_key_release(self, key, modifiers):
        ''''''
        pass

    def on_update(self, delta_time):
        ''''''
        pass

    def on_draw(self):
        ''''''
        pass


class Menu(GameState):
    def __init__(self, context=None) -> None:
        ''''''
        self.context = context
        toprow = self.context.height - 226
        offset = self.context.grid_height
        self.label1 = Label("", x=20, y=toprow-offset*0, font_size=15, color=(200,200,200,255),)
        self.label2 = Label("", x=20, y=toprow-offset*1, font_size=15, color=(200,200,200,255),)
        self.label3 = Label("", x=20, y=toprow-offset*2, font_size=15, color=(200,200,200,255),)
        self.label4 = Label("", x=20, y=toprow-offset*3, font_size=15, color=(200,200,200,255),)
        self.label5 = Label("", x=20, y=toprow-offset*4, font_size=15, color=(200,200,200,255),)
        
        self.label1.text = f"TETR1S"
        self.label2.text = f"Press [SPACE] to Start"
        self.label3.text = f"Press [ESCAPE] to escape"
        self.label4.text = f"Up/Down sets speed: {Running.speed}"
        self.label5.text = f"TETR1S"

    def set_context(self, context):
        self.context = context

    def on_key_press(self, key, modifiers):
        ''''''
        if key == window.key.LEFT:
            self.left_key()
        if key == window.key.RIGHT:
            self.right_key()
        if key == window.key.UP:
            self.up_key()
        if key == window.key.DOWN:
            self.down_key()
        if key == window.key.SPACE:
            self.space_key()
        if key == window.key.ESCAPE:
            exit()

    def on_key_release(self, key, modifiers):
        ''''''
        pass

    def on_update(self, delta_time):
        ''''''
        pass

    def on_draw(self):
        ''''''
        self.label1.draw()
        self.label2.draw()
        self.label3.draw()
        self.label4.draw()
        self.label5.draw()

    def space_key(self):
        ''''''
        self.context.set_state(Running(new_game=True,context=self.context))

    def left_key(self):
        ''''''
        pass

    def right_key(self):
        ''''''
        pass

    def up_key(self):
        ''''''
        Running.speed += 1
        if Running.speed > 5:
            Running.speed = 5
        self.label4.text = f"Up/Down sets speed: {Running.speed}"

    def down_key(self):
        ''''''
        Running.speed -= 1
        if Running.speed < 1:
            Running.speed = 1
        self.label4.text = f"Up/Down sets speed: {Running.speed}"


class Running(GameState):
    '''Game state for gameplay. Draws playground, handles shapes, scores, etc'''
    score = 0
    speed = 1

    def __init__(self, new_game=True, context=None) -> None:
        ''''''
        self.context = context
        self.grid_width = self.context.grid_width
        self.grid_height = self.context.grid_height
        self.left_border = 7     # conclusive
        self.right_border = 15
        map_width = self.right_border - self.left_border
        map_height = (self.context.height // self.context.grid_height)
        self.label = Label("", x=20, y=self.context.height-226, font_size=15, color=(200,200,200,255),)
        if new_game:
            Running.score = 0
        self.shapes = Shapes()
        self.playground = Map(map_width, map_height)
        self.prev_time = time()
        self.black_box = SolidColorImagePattern((0,0,0,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.red_box = SolidColorImagePattern((220,150,110,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.red_inner_box = SolidColorImagePattern((220,110,70,255)).create_image(self.grid_width-3,self.grid_height-3)
        self.green_box = SolidColorImagePattern((100,240,100,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.blue_box = SolidColorImagePattern((110,150,220,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.blue_inner_box = SolidColorImagePattern((70,110,220,255)).create_image(self.grid_width-3,self.grid_height-3)
        self.playground.update_player_shape(0,0)
        self.stuck = 0

    def set_context(self, context):
        self.context = context

    def draw_playground(self):
        col = self.left_border
        row = 0
        for x in range(self.left_border*self.grid_width, self.right_border*self.grid_width, self.grid_width):
            for y in range(0, self.context.height, self.grid_height):
                # middle green playground
                if self.left_border<=col and col<self.right_border:
                    self.context.image.blit_into(self.green_box, x+1, y+1, 0)
                    # tetris tetrominoes
                    scene_coords = (col-self.left_border, row)
                    grid_color = self.playground.get_grid_color(*scene_coords)
                    if grid_color == "blue":
                        self.context.image.blit_into(self.blue_box, x+1, y+1, 0)
                        self.context.image.blit_into(self.blue_inner_box, x+1, y+3, 0)
                        #self.context.image.blit_into(self.white_pixel, x+1, y+self.grid_height-2, 0)
                        #self.context.image.blit_into(self.white_pixel, x+3, y+self.grid_height-4, 0)
                        #self.context.image.blit_into(self.white_pixel, x+3, y+self.grid_height-6, 0)
                        #self.context.image.blit_into(self.white_pixel, x+5, y+self.grid_height-4, 0)
                    if grid_color == "red":
                        self.context.image.blit_into(self.red_box, x+1, y+1, 0)
                        self.context.image.blit_into(self.red_inner_box, x+1, y+3, 0)
                    if grid_color == 'black':
                        self.context.image.blit_into(self.black_box, x+1, y+1, 0)
                row += 1
            col += 1
            row = 0

    def on_key_press(self, key, modifiers):
        ''''''
        if key == window.key.LEFT:
            self.left_key()
        if key == window.key.RIGHT:
            self.right_key()
        if key == window.key.DOWN:
            self.down_key()
        if key == window.key.SPACE:
            self.space_key()
        if key == window.key.ESCAPE:
            self.esc_key()
        if key == window.key.S:
            self.s_key()

    def on_key_release(self, key, modifiers):
        ''''''
        pass

    def on_update(self, delta_time):
        ''''''
        self.label.text = f"Speed: {Running.speed}   Score: {Running.score}"
        min_delay = 1/Running.speed
        if time() - self.prev_time > min_delay and not self.playground.full:
            if not self.playground.update_player_shape(0,-1):
                self.stuck += 1
                if self.stuck >= 2:
                    self.playground.lock_player_shape()
                    self.playground.generate_new_shape()
                    self.stuck = 0
            self.prev_time = time()
        if self.playground.full:
            self.label.text = f"Game Over! Score: {Running.score}"

    def on_draw(self):
        ''''''
        self.draw_playground()
        self.label.draw()

    def esc_key(self):
        self.context.set_state(Menu(self.context))

    def s_key(self):
        self.context.set_state(Scores(self.context))

    def space_key(self):
        Running.score += 1
        self.playground.rotate_player()
        self.draw_playground()

    def left_key(self):
        self.playground.update_player_shape(-1,0)
        self.draw_playground()

    def right_key(self):
        self.playground.update_player_shape(1,0)
        self.draw_playground()

    def down_key(self):
        self.playground.update_player_shape(0,-1)
        self.draw_playground()


class Scores(GameState):
    max_score = 0
    def __init__(self, context=None) -> None:
        ''''''
        self.context = context
        self.label = Label(f"High Score: {Scores.max_score}", x=20, y=self.context.height-226, font_size=15, color=(200,200,200,255),)

    def set_context(self, context):
        self.context = context

    def on_key_press(self, key, modifiers):
        ''''''
        if key == window.key.SPACE:
            self.space_key()
        if key == window.key.ESCAPE:
            self.esc_key()

    def on_update(self, delta_time):
        ''''''
        Scores.max_score = max(Scores.max_score, Running.score)
        self.label.text = f"High Score: {Scores.max_score}"

    def on_draw(self):
        ''''''
        self.label.draw()

    def esc_key(self):
        self.context.set_state(Menu(self.context))

    def space_key(self):
        self.context.set_state(Running(new_game=False,context=self.context))