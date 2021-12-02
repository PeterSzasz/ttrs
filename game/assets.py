
# tetris map represented by a 2d array

class Map:
    def __init__(self, map_width=10, map_height=20) -> None:
        self.map_width = map_width
        self.map_height = map_height
        self.table = [[None]*map_height for _ in range(map_width)]
        self.test_assets()
        
    def check_grid(self, x, y):
        '''
        input:
        x: [int] starts with 0
        y: [int] starts with 0
        '''
        if  0<=x and x<self.map_width and \
            0<=y and y<self.map_height and \
            self.table[x][y] is not None:
                return self.table[x][y]
        return None

    def color_grid(self, x, y, color):
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
        self.tetriminos = {
            'box':{'shape':[(-1,-1),(0,-1),(0,0),(-1,0)],'bottom_left':(-1,-1),'top_right':(0,0),'color':'red'},
            'L-shape':{'shape':[(-1,-1),(0,-1),(0,0),(0,1)],'bottom_left':(-1,-1),'top_right':(0,1),'color':'red'}
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
        if shape in self.tetriminos.keys():
            shape_coords = self.tetriminos[shape]['shape']
            new_shape_coords = []
            for coord in shape_coords:
                if clockwise:                    
                    new_shape_coords.append( (coord[1],-1*coord[0]) )
                else:
                    new_shape_coords.append( (-1*coord[1],coord[0]) )
            self.tetriminos[shape]['shape'] = new_shape_coords
        min_coord = (100,100)
        max_coord = (-100,-100)
        for coord in self.tetriminos[shape]['shape']:
            if coord < min_coord: min_coord = coord
            if max_coord < coord: max_coord = coord
        self.tetriminos[shape]['bottom_left'] = min_coord
        self.tetriminos[shape]['top_right'] = max_coord

if __name__ == '__main__':
    ts = Shapes()
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])