class Direction:
    def __init__(self):
        self.UP = (-1,0)
        self.DOWN = (1, 0)
        self.LEFT = (0, -1)
        self.RIGHT = (0, 1)
        
    def directionsList(self):
        return [self.UP, self.DOWN, self.LEFT, self.RIGHT]
    

dirs = Direction()