# 
# tetris map represented by a 2d array
# 

class Map:
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
        print(f"min coord: {min_coord}")
        print(f"max coord: {max_coord}")

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