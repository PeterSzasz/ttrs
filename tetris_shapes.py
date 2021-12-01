

class TetrisShapes:
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
    ts = TetrisShapes()
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])
    ts.rotate('box')
    print(ts.tetriminos['box'])