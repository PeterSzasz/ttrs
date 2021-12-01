#
#
#

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
        self.label = Label("", x=20, y=self.context.height-25, font_size=15, color=(200,200,200,255),)

    def set_context(self, context):
        self.context = context

    def on_key_press(self, key, modifiers):
        ''''''
        if key == window.key.LEFT:
            print("LEFT")
            self.left_key()
        if key == window.key.RIGHT:
            print("RIGHT")
            self.right_key()
        if key == window.key.UP:
            print("UP")
            self.up_key()
        if key == window.key.DOWN:
            print("DOWN")
            self.down_key()
        if key == window.key.SPACE:
            print("SPACE")
            self.context.set_state(Running(self.context))
        if key == window.key.ESCAPE:
            exit()

    def on_key_release(self, key, modifiers):
        ''''''
        pass

    def on_update(self, delta_time):
        ''''''
        self.label.text = f"TETR1S {delta_time}"

    def on_draw(self):
        ''''''
        self.label.draw()

    def space_key(self):
        ''''''
        pass

    def left_key(self):
        ''''''
        pass

    def right_key(self):
        ''''''
        pass

    def up_key(self):
        ''''''
        pass

    def down_key(self):
        ''''''
        pass


class Running(GameState):
    '''Game state for gameplay. Draws playground, handles shapes, scores, etc'''
    score = 0
    level = 1

    def __init__(self, context=None) -> None:
        ''''''
        self.context = context
        self.test_shape = 'L-shape'
        self.label = Label("", x=20, y=self.context.height-25, font_size=15, color=(200,200,200,255),)
        self.grid_width = self.context.grid_width
        self.grid_height = self.context.grid_height
        self.left_border = 7     # conclusive
        self.right_border = 15
        map_width = self.right_border - self.left_border
        map_height = (self.context.height // self.context.grid_height)
        self.shapes = Shapes()
        self.playground = Map(map_width, map_height)
        self.player_pivot = (map_width//2,map_height-5)

        self.black_box = SolidColorImagePattern((0,0,0,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.red_box = SolidColorImagePattern((220,150,110,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.red_inner_box = SolidColorImagePattern((220,110,70,255)).create_image(self.grid_width-3,self.grid_height-3)
        self.green_box = SolidColorImagePattern((100,240,100,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.blue_box = SolidColorImagePattern((110,150,220,255)).create_image(self.grid_width-1,self.grid_height-1)
        self.blue_inner_box = SolidColorImagePattern((70,110,220,255)).create_image(self.grid_width-3,self.grid_height-3)

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
                    # tetris tetriminos
                    scene_coords = (col-self.left_border, row)
                    grid_color = self.playground.check_grid(*scene_coords)
                    if grid_color is not None:
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
                            #self.context.image.blit_into(self.white_pixel, x+1, y+self.grid_height-2, 0)
                            #self.context.image.blit_into(self.white_pixel, x+3, y+self.grid_height-4, 0)
                            #self.context.image.blit_into(self.white_pixel, x+3, y+self.grid_height-6, 0)
                            #self.context.image.blit_into(self.white_pixel, x+5, y+self.grid_height-4, 0)
                        if grid_color == 'black':
                            self.context.image.blit_into(self.black_box, x+1, y+1, 0)
                row += 1
            col += 1
            row = 0

    def update_pivot(self, clear=False):
        t_minos = self.shapes.tetriminos[self.test_shape]
        for box in t_minos['shape']:
            color = t_minos['color']
            x = self.player_pivot[0] + box[0]
            y = self.player_pivot[1] + box[1]
            if  0<=x and x<self.context.width and \
                0<=y and y<self.context.height:
                    if clear:
                        self.playground.color_grid(x,y,None)
                    else:
                        self.playground.color_grid(x,y,color)

    def on_key_press(self, key, modifiers):
        ''''''
        if key == window.key.LEFT:
            print("LEFT")
            self.left_key()
        if key == window.key.RIGHT:
            print("RIGHT")
            self.right_key()
        if key == window.key.UP:
            print("UP")
            self.up_key()
        if key == window.key.DOWN:
            print("DOWN")
            self.down_key()
        if key == window.key.SPACE:
            print("SPACE")
            self.space_key()
        if key == window.key.ESCAPE:
            self.context.set_state(Menu(self.context))
        if key == window.key.S:
            self.context.set_state(Scores(self.context))

    def on_key_release(self, key, modifiers):
        ''''''
        pass

    def on_update(self, delta_time):
        ''''''
        self.label.text = f"Level: {Running.level}  Score: {Running.score}"

    def on_draw(self):
        ''''''
        #self.update_pivot()
        self.draw_playground()
        self.label.draw()

    def space_key(self):
        Running.score += 1
        self.update_pivot(clear=True)
        self.shapes.rotate(self.test_shape)
        self.update_pivot()
        self.draw_playground()

    def left_key(self):
        self.update_pivot(clear=True)
        self.player_pivot = (self.player_pivot[0]-1,self.player_pivot[1])
        self.update_pivot()
        self.draw_playground()

    def right_key(self):
        self.update_pivot(clear=True)
        self.player_pivot = (self.player_pivot[0]+1,self.player_pivot[1])
        self.update_pivot()
        self.draw_playground()

    def up_key(self):
        self.update_pivot(clear=True)
        self.player_pivot = (self.player_pivot[0],self.player_pivot[1]+1)
        self.update_pivot()
        self.draw_playground()

    def down_key(self):
        self.update_pivot(clear=True)
        self.player_pivot = (self.player_pivot[0],self.player_pivot[1]-1)
        self.update_pivot()
        self.draw_playground()


class Scores(GameState):
    def __init__(self, context=None) -> None:
        ''''''
        self.context = context
        self.label = Label(f"High Scores: {Running.score}", x=20, y=self.context.height-25, font_size=15, color=(200,200,200,255),)

    def set_context(self, context):
        self.context = context

    def on_key_press(self, key, modifiers):
        ''''''
        if key == window.key.SPACE:
            print("SPACE")
            self.context.set_state(Menu(self.context))
        if key == window.key.ESCAPE:
            print("ESC")
            self.context.set_state(Menu(self.context))

    def on_key_release(self, key, modifiers):
        ''''''
        pass

    def on_update(self, delta_time):
        ''''''
        pass

    def on_draw(self):
        ''''''
        self.label.draw()

    def space_key(self):
        ''''''
        pass

    def left_key(self):
        ''''''
        pass

    def right_key(self):
        ''''''
        pass

    def up_key(self):
        ''''''
        pass

    def down_key(self):
        ''''''
        pass