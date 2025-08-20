from game.Board import Board
from solver.Solver import solve
from ui.BoardViewer import BoardViewer
from game.Constants import dirs

def main():
    #start = (0, 0)
    #end = (5, 5)
    numbers = [(0,0), (5,5), (4,1), (2,1), (3,4), (3,2), (1,4), (2,3)]
    borders = [[dirs.DOWN, 0, 0], [dirs.DOWN, 0, 1], [dirs.DOWN, 0, 2]]
    board = Board(6, numbers)
    path = solve(board)
    path.append(numbers[-1])
    bv = BoardViewer(board, path)
    bv.show()
    
if __name__ == '__main__':
    main()