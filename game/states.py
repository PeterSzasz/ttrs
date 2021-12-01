#
#
#

from pyglet import window
from pyglet.app import exit

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
    def __init__(self) -> None:
        ''''''
        pass

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
            exit()
        if key == window.key.P:
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

    def space_key(self):
        pass

    def left_key(self):
        pass

    def right_key(self):
        pass

    def up_key(self):
        pass

    def down_key(self):
        pass


class Running(GameState):
    def __init__(self) -> None:
        ''''''
        pass

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
            exit()
        if key == window.key.P:
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

    def space_key(self):
        if self.game_mode == "running": # and rotating doesn't collide with border
            self.update_pivot(clear=True)
            self.shapes.rotate(self.test_shape)
            self.update_pivot()
            self.draw_playground()

    def left_key(self):
        if self.game_mode == "running" and 0 < self.player_pivot[0]+self.shapes.tetriminos[self.test_shape]['bottom_left'][0]:
            self.update_pivot(clear=True)
            self.player_pivot = (self.player_pivot[0]-1,self.player_pivot[1])
            self.update_pivot()
            self.draw_playground()

    def right_key(self):
        if self.game_mode == "running"and self.player_pivot[0]+self.shapes.tetriminos[self.test_shape]['top_right'][0] < MAP_WIDTH-1:
            self.update_pivot(clear=True)
            self.player_pivot = (self.player_pivot[0]+1,self.player_pivot[1])
            self.update_pivot()
            self.draw_playground()

    def up_key(self):
        if self.game_mode == "running" and self.player_pivot[1]+self.shapes.tetriminos[self.test_shape]['top_right'][1] < (self.height//GRID_HEIGHT)-1:
            self.update_pivot(clear=True)
            self.player_pivot = (self.player_pivot[0],self.player_pivot[1]+1)
            self.update_pivot()
            self.draw_playground()

    def down_key(self):
        if self.game_mode == "running" and 0 < self.player_pivot[1]-self.shapes.tetriminos[self.test_shape]['bottom_left'][1]:
            self.update_pivot(clear=True)
            self.player_pivot = (self.player_pivot[0],self.player_pivot[1]-1)
            self.update_pivot()
            self.draw_playground()


class Scores(GameState):
    def __init__(self) -> None:
        ''''''
        pass

    def on_key_press(self, key, modifiers):
        ''''''
        if key == key.SPACE:
            print("SPACE")
            self.space_key()
        if key == key.ESCAPE:
            exit()

    def on_key_release(self, key, modifiers):
        ''''''
        pass

    def on_update(self, delta_time):
        ''''''
        pass

    def on_draw(self):
        ''''''
        pass

    def space_key(self):
        pass

    def left_key(self):
        pass

    def right_key(self):
        pass

    def up_key(self):
        pass

    def down_key(self):
        pass