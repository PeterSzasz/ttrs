# tetris main window, menu, scores, game scene, icons, etc
import pyglet
from game_scene import GameScene

# window settings
SCREEN_TITLE = "Tetris in Arcade"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameWindow(pyglet.window.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        super(GameWindow, self).__init__(width=width, height=height, caption=title)
        self.gsc = GameScene(SCREEN_WIDTH, SCREEN_HEIGHT)
        
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == pyglet.window.key.LEFT:
            print("LEFT")
            self.gsc.left_key()
        if key == pyglet.window.key.RIGHT:
            print("RIGHT")
            self.gsc.right_key()
        if key == pyglet.window.key.UP:
            print("UP")
            self.gsc.up_key()
        if key == pyglet.window.key.DOWN:
            print("DOWN")
            self.gsc.down_key()
        if key == pyglet.window.key.SPACE:
            print("SPACE")
            self.gsc.space_key()
        if key == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
        if key == pyglet.window.key.P:
            pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
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
