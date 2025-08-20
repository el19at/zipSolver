from game.Constants import dirs


class Cell:
    def __init__(self, value=0, borders=None):
        self.value: int = value
        self.borders: list[list[int]] = borders if borders else []

    def canMove(self, direction):
        return direction not in self.borders
    
    def validMoves(self):
        return [direction for direction in dirs if self.canMove(direction)]
    
    def addBorder(self, direction):
        if direction not in self.borders:
            self.borders.append(direction)
    
    def isNumber(self):
        return self.value > 0