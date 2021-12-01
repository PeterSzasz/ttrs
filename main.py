# tetris main window, menu, scores, game scene, icons, etc
import pyglet
from game.scene import GUI

# window settings
SCREEN_TITLE = "Tetris in Arcade"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameWindow(pyglet.window.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        super(GameWindow, self).__init__(width=width, height=height, caption=title)
        self.gsc = GUI(SCREEN_WIDTH, SCREEN_HEIGHT)
     
    def on_key_press(self, key, modifiers):
        self.gsc.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        pass

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.gsc.draw()
                


if __name__ == "__main__":
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    pyglet.app.run()
