
# tetris main window, state initialization, main loop start

import sys
from os import chdir
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    chdir(sys._MEIPASS)

from pyglet.window import Window
from pyglet import app, clock
from game.scene import GUI
from game.states import Menu, Running, Scores

SCREEN_TITLE = "Tetris in pyglet"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameWindow(Window):
    """ Main Window """

    def __init__(self, width, height, title):
        super(GameWindow, self).__init__(width=width, height=height, caption=title)
        self.gui = GUI(SCREEN_WIDTH, SCREEN_HEIGHT)
        initial_state = Menu(self.gui)
        self.gui.set_state(initial_state)
     
    def on_key_press(self, key, modifiers):
        self.gui.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.gui.on_update(delta_time)

    def on_draw(self):
        """ Draw everything """
        self.gui.on_draw()


if __name__ == "__main__":
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    clock.schedule_interval(window.on_update, 0.1)
    app.run()
