from game.Cell import Cell
from game.Board import Board
from game.Constants import dirs
from solver.Tree import Tree

def findPath(
    board: Board,
    start: tuple[int],
    end: tuple[int],
    visited: set[tuple[int]],
    path: list[tuple[int]],
    lastNumber: int
    ):
    if start == end and len(path) == board.dimension**2 - 1:
        return [True, path]
    if start == end:
        return [False, None]
    
    cell: Cell = board.grid[start[0]][start[1]]
    if cell.isNumber():
        if cell.value - lastNumber == 1:
            lastNumber = cell.value
        else:
            return [False, None]
    visited.add(start)
    path.append(start)
    allMoves = board.getAllMoves(start[0], start[1])
    res = []
    for move in allMoves:
        if move in visited:
            continue
        res.append(findPath(board, move, end, set([item for item in list(visited)]), [item for item in path], lastNumber))
    for finalRes in res:
        if finalRes[0]:
            return finalRes
    return [False, None]

def solve(board: Board) -> list[tuple[int]]:
    visited = set([])
    numbersIndxs = getNumsInds(board)
    start = numbersIndxs[1]
    end = numbersIndxs[len(numbersIndxs)]
    return findPath(board, start, end, visited, [], 0)[1]
    

def getNumsInds(board: Board):
    inds = {}
    for i, row in enumerate(board.grid):
        for j, cell in enumerate(row):
            if cell.value > 0:
                inds[cell.value] = (i, j)
    return inds