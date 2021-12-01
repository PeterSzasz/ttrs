
# tetris map represented by 2d array

class TetrisMap:
    def __init__(self, map_width=10, map_height=20) -> None:
        self.map_width = map_width
        self.map_height = map_height
        self.map = [[None]*map_height for _ in range(map_width)]
        self.test_assets()
        
    def check_grid(self, x, y):
        '''
        input:
        x: [int] starts with 0
        y: [int] starts with 0
        '''
        if  0<=x and x<self.map_width and \
            0<=y and y<self.map_height and \
            self.map[x][y] is not None:
                #print(f"checking: {x} {y} {self.map[x][y]}")
                return self.map[x][y]
        #print(f"checking: {x} {y}")
        return None

    def color_grid(self, x, y, color):
        if  0<=x and x<self.map_width and \
            0<=y and y<self.map_height and \
            (color == 'red' or color == 'blue' or color == None):
                self.map[x][y] = color


    def test_assets(self):
        # L shape
        self.map[0][0] = "red"
        self.map[1][0] = "red"
        self.map[1][1] = "red"
        self.map[1][2] = "red"
        # box shape
        self.map[2][5] = "red"
        self.map[2][6] = "red"
        self.map[3][5] = "red"
        self.map[3][6] = "red"
        # vertival line
        self.map[5][1] = "blue"
        self.map[5][2] = "blue"
        self.map[5][3] = "blue"
        self.map[5][4] = "blue"
        # Z shape
        self.map[2][8] = "blue"
        self.map[3][8] = "blue"
        self.map[3][9] = "blue"
        self.map[4][9] = "blue"
        # T shape
        self.map[self.map_width-1][self.map_height-1] = "red"
        self.map[self.map_width-1][self.map_height-2] = "red"
        self.map[self.map_width-2][self.map_height-2] = "red"
        self.map[self.map_width-1][self.map_height-3] = "red"

        #for i in range(self.map_width):
        #    for j in range(self.map_height):
        #        print(f"{i}:{j} = {self.map[i][j]}")

