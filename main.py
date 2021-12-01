# tetris main window, menu, scores, game scene, icons, etc
from pyglet.window import Window
from pyglet import app, clock
from game.scene import GUI
from game.states import GameState, Menu, Running, Scores

# window settings
SCREEN_TITLE = "Tetris in Arcade"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameWindow(Window):
    """ Main Window """

    def __init__(self, width, height, title):
        super(GameWindow, self).__init__(width=width, height=height, caption=title)
        self.gui = GUI(SCREEN_WIDTH, SCREEN_HEIGHT)
        initial_state = Running(self.gui)
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
        self.clear()
        self.gui.on_draw()
                


if __name__ == "__main__":
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    clock.schedule_interval(window.on_update, 0.1)
    app.run()
