
# tetris map represented by a 2d array

import random

class Map:
    def __init__(self, map_width=10, map_height=20) -> None:
        self.map_width = map_width
        self.map_height = map_height
        self.shapes = Shapes()
        self.table = [[None]*map_height for _ in range(map_width)]
        rand_shape = random.choice(list(self.shapes.tetrominoes.keys()))
        self.player_shape = self.shapes.tetrominoes[rand_shape]
        self.player_pivot = (map_width//2,map_height-1)
        self.full = False
        #self.test_assets()
        
    def update_player_shape(self, offset_x, offset_y ):
        valid = True
        for grid in self.player_shape['coords']:
            x = self.player_pivot[0] + grid[0] + offset_x
            y = self.player_pivot[1] + grid[1] + offset_y
            if not self.is_valid(x,y):
                valid = False
        if valid:
            for grid in self.player_shape['coords']:
                x = self.player_pivot[0] + grid[0]
                y = self.player_pivot[1] + grid[1]
                self.color_grid(x,y,None)
            self.player_pivot = (self.player_pivot[0] + offset_x, self.player_pivot[1] + offset_y)
            color = self.player_shape['color']
            for grid in self.player_shape['coords']:
                x = self.player_pivot[0] + grid[0]
                y = self.player_pivot[1] + grid[1]
                self.color_grid(x,y,color)
        print(f"valid: {valid}")
        return valid

    def lock_player_shape(self):
        print(self.player_pivot)
        for grid in self.player_shape['coords']:
            x = self.player_pivot[0] + grid[0]
            y = self.player_pivot[1] + grid[1]
            self.color_grid(x,y,'blue')
            print(f'blue: {x}:{y}')

    def generate_new_shape(self):
        rand_shape = random.choice(list(self.shapes.tetrominoes.keys()))
        self.player_shape = self.shapes.tetrominoes[rand_shape]
        x = self.map_width//2
        y = self.map_height-1
        if self.is_valid(x,y):
            self.player_pivot = (x,y)
        elif self.is_valid(x-2,y):
            self.player_pivot = (x-2,y)
        elif self.is_valid(x+2,y):
            self.player_pivot = (x+2,y)
        else:
            self.full = True

    def rotate_player(self, clockwise=True):
        new_shape_coords = []
        valid = True
        for coord in self.player_shape['coords']:
            if clockwise:                    
                new_shape_coords.append( (coord[1],-1*coord[0]) )
            else:
                new_shape_coords.append( (-1*coord[1],coord[0]) )
        for grid in new_shape_coords:
            if not self.is_valid(self.player_pivot[0] + grid[0],self.player_pivot[1] + grid[1]):
                valid = False
        if valid:
            for grid in self.player_shape['coords']:
                x = self.player_pivot[0] + grid[0]
                y = self.player_pivot[1] + grid[1]
                self.color_grid(x,y,None)
            self.player_shape['coords'] = new_shape_coords
            color = self.player_shape['color']
            for grid in self.player_shape['coords']:
                x = self.player_pivot[0] + grid[0]
                y = self.player_pivot[1] + grid[1]
                self.color_grid(x,y,color)

    def is_valid(self, x, y):
        '''
        input:
        x: [int] starts with 0
        y: [int] starts with 0
        '''
        if  0<=x and x<self.map_width and 0<=y:
            if y<self.map_height and self.table[x][y] == 'blue':
                return False
            else:
                return True
        return False

    def get_grid_color(self, x, y):
        '''
        input:
        x: [int] starts with 0
        y: [int] starts with 0
        '''
        if 0<=x and x<self.map_width and 0<=y and y<self.map_height \
            and self.table[x][y] is not None:
                return self.table[x][y]
        return None

    def is_row_filled(self, row):
        ''''''
        filled = True
        y = row
        for x in range(self.map_width):
            if self.table[x][y] is None:
                filled = False
        return filled

    def color_grid(self, x, y, color):
        ''''''
        if  0<=x and x<self.map_width and \
            0<=y and y<self.map_height and \
            (color == 'red' or color == 'blue' or color == None):
                self.table[x][y] = color

    def test_assets(self):
        # L shape
        self.table[0][0] = "red"
        self.table[1][0] = "red"
        self.table[1][1] = "red"
        self.table[1][2] = "red"
        # box shape
        self.table[2][5] = "red"
        self.table[2][6] = "red"
        self.table[3][5] = "red"
        self.table[3][6] = "red"
        # vertival line
        self.table[5][1] = "blue"
        self.table[5][2] = "blue"
        self.table[5][3] = "blue"
        self.table[5][4] = "blue"
        # Z shape
        self.table[2][8] = "blue"
        self.table[3][8] = "blue"
        self.table[3][9] = "blue"
        self.table[4][9] = "blue"
        # T shape
        self.table[self.map_width-1][self.map_height-1] = "red"
        self.table[self.map_width-1][self.map_height-2] = "red"
        self.table[self.map_width-2][self.map_height-2] = "red"
        self.table[self.map_width-1][self.map_height-3] = "red"

        #for i in range(self.map_width):
        #    for j in range(self.map_height):
        #        print(f"{i}:{j} = {self.map[i][j]}")


class Shapes:
    def __init__(self) -> None:
        self.tetrominoes = {
            'box':{'coords':[(-1,-1),(0,-1),(0,0),(-1,0)],'bottom_left':(-1,-1),'top_right':(0,0),'color':'red'},
            'L-shape':{'coords':[(-1,-1),(0,-1),(0,0),(0,1)],'bottom_left':(-1,-1),'top_right':(0,1),'color':'red'},
            'line':{'coords':[(0,-2),(0,-1),(0,0),(0,1)],'bottom_left':(0,-2),'top_right':(0,1),'color':'red'},
            'T-shape':{'coords':[(-1,-1),(0,-1),(1,-1),(0,0)],'bottom_left':(-1,-1),'top_right':(1,0),'color':'red'},
            'Z-shape':{'coords':[(-1,-1),(0,-1),(0,0),(1,0)],'bottom_left':(-1,-1),'top_right':(1,0),'color':'red'}
            }

    def rotate(self, shape, clockwise=True):
        '''
        Rotate right (by default) or left 90 degree the given shape.
        rot matrix for 90degr: [(0,-1),(1,0)]
        rot matrix for -90degr: [(0,1),(-1,0)]
        cw: sin(90)=-1 cos(90)=0
        cc: sin(90)=1 cos(90)=0
        [cos]
        '''
        if shape in self.tetrominoes.keys():
            shape_coords = self.tetrominoes[shape]['coords']
            new_shape_coords = []
            for coord in shape_coords:
                if clockwise:                    
                    new_shape_coords.append( (coord[1],-1*coord[0]) )
                else:
                    new_shape_coords.append( (-1*coord[1],coord[0]) )
            self.tetrominoes[shape]['coords'] = new_shape_coords
        min_coord = (100,100)
        max_coord = (-100,-100)
        for coord in self.tetrominoes[shape]['coords']:
            if coord < min_coord: min_coord = coord
            if max_coord < coord: max_coord = coord
        self.tetrominoes[shape]['bottom_left'] = min_coord
        self.tetrominoes[shape]['top_right'] = max_coord

if __name__ == '__main__':
    ts = Shapes()
    print(ts.tetrominoes['box'])
    ts.rotate('box')
    print(ts.tetrominoes['box'])
    ts.rotate('box')
    print(ts.tetrominoes['box'])
    ts.rotate('box')
    print(ts.tetrominoes['box'])
    ts.rotate('box')
    print(ts.tetrominoes['box'])