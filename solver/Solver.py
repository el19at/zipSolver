import random
from game.Cell import Cell
from game.Board import Board
from ui.BoardViewer import BoardViewer
from bs4 import BeautifulSoup

WALL_MAP = {
    "trail-cell-wall--up": [(-1, 0)],
    "trail-cell-wall--down": [(1, 0)],
    "trail-cell-wall--left": [(0, -1)],
    "trail-cell-wall--right": [(0, 1)],
}

def findPath(
    board: Board,
    start: tuple[int],
    end: tuple[int],
    visited: set[tuple[int]],
    path: list[tuple[int]],
    lastNumber: int,
    display: bool = False
    ):
    if start == end and len(path) == board.dimension**2 - 1:
        return [True, path]
    if start == end:
        if display:
            displayBoard(board, path)
        return [False, None]
    
    cell: Cell = board.grid[start[0]][start[1]]
    if cell.isNumber():
        if cell.value - lastNumber == 1:
            lastNumber = cell.value
        else:
            if display:
                displayBoard(board, path)
            return [False, None]
    visited.add(start)
    path.append(start)
    allMoves = board.getAllMoves(start[0], start[1])
    random.shuffle(allMoves)
    res = []
    for move in allMoves:
        if move in visited:
            continue
        res.append(findPath(board, move, end, set([item for item in list(visited)]), [item for item in path], lastNumber, display))
    for finalRes in res:
        if finalRes[0]:
            if display:
                displayBoard(board, path)
            return finalRes
    
    if display:
        displayBoard(board, path)
    return [False, None]

def solve(board: Board) -> list[tuple[int]]:
    visited = set([])
    numbersIndxs = getNumsInds(board)
    start = numbersIndxs[1]
    end = numbersIndxs[len(numbersIndxs)]
    return findPath(board, start, end, visited, [], 0, False)[1] + [end]
    

def getNumsInds(board: Board):
    inds = {}
    for i, row in enumerate(board.grid):
        for j, cell in enumerate(row):
            if cell.value > 0:
                inds[cell.value] = (i, j)
    return inds


def html_to_board(html_text: str) -> Board:
    soup = BeautifulSoup(html_text, "html.parser")
    
    # Find the grid container to get dimensions
    grid = soup.find("div", class_="trail-grid")
    rows = int(grid.get("style").split("--rows:")[1].split(";")[0])
    cols = int(grid.get("style").split("--cols:")[1].split(";")[0])
    
    numbersList = []
    borderList = []
    
    # Process each cell
    for cell_div in grid.find_all("div", class_="trail-cell"):
        cell_idx = int(cell_div["data-cell-idx"])
        x = cell_idx // cols
        y = cell_idx % cols
        
        # Extract number if present
        content_div = cell_div.find("div", class_="trail-cell-content")
        if content_div and content_div.text.strip().isdigit():
            val = content_div.text.strip()
            numbersList.append([val, (x, y)])
        # Extract walls
        for wall_div in cell_div.find_all("div", class_="trail-cell-wall"):
            classes = wall_div.get("class", [])
            for cls in classes:
                if cls in WALL_MAP:
                    for direction in WALL_MAP[cls]:
                        borderList.append([direction, x, y])
    numbersList.sort(key=sortFunc)
    numbersList = [item[1] for item in numbersList]
    return Board(dimension=rows, numbersList=numbersList, borderList=borderList)
def sortFunc(element):
    return element[0]
def displayBoard(board: Board, path: list[tuple[int]]):
    bv = BoardViewer(board, path)
    bv.show(500)