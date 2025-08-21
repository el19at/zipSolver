from game.Cell import Cell
from game.Constants import dirs

class Board():
    def __init__(self, dimension:int , numbersList: list[tuple[int]] = [], borderList: list[list]=[]):
        self.grid:list[list[Cell]] = []
        for _ in range(dimension):
            row = []
            for __ in range(dimension):
                cell = Cell()
                row.append(cell)
            self.grid.append(row)
                
        self.dimension = dimension
        
        for i, ind in enumerate(numbersList):
            x, y = ind
            self.grid[x][y].value = i+1
            
        for direction, x, y in borderList:
            cell: Cell = self.grid[x][y]
            cell.addBorder(direction)

            # compute neighbor indices directly
            nx, ny = x + direction[0], y + direction[1]
            if 0 <= nx < self.dimension and 0 <= ny < self.dimension:
                neib: Cell = self.grid[nx][ny]
                opposite = (-direction[0], -direction[1])
                neib.addBorder(opposite)



        
    def printGrid(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                print('({}, {}): {}'.format(i, j, cell.borders))
                            
    def getMoveInds(self, i, j, direction) -> tuple[int] | None:
        x = i + direction[0]
        y = j + direction[1]
        return (x, y) if self.inRange(x, y) and self.grid[i][j].canMove(direction) else None
    
    def getMoveCell(self, i, j, direction) -> Cell | None:
        inds = self.getMoveInds(i, j, direction)
        if not inds:
            return None
        x, y = inds
        return self.grid[x][y]
    
    def getAllMoves(self, i, j) -> list[tuple[int]]:
        res = []
        for dir in dirs.directionsList():
            ind = self.getMoveInds(i, j, dir)
            if ind:
                res.append(ind)
        return res
    
    def inRange(self, i, j):
        return 0 <= i < self.dimension and 0 <= j < self.dimension