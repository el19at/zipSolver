# LinkedIn Zip Game Solver

A Python project that automatically fetches and solves the **LinkedIn Zip game**, displaying the solution path on a visual board.  

This project uses **Playwright** for browser automation, **BeautifulSoup** for HTML parsing, and a custom solver to calculate the optimal path through the numbered grid.

---

## Features

- Automates opening the LinkedIn Zip game in a browser.
- Clicks the **Start Game** button automatically.
- Parses the game grid directly from the iframe.
- Solves the puzzle using a custom algorithm.
- Visualizes the solution path using `BoardViewer`.

---

## Requirements

- Python 3.10+
- [Playwright](https://playwright.dev/python/)
- BeautifulSoup4
- Matplotlib (for board visualization)
- Optional: Selenium if you prefer alternative automation

Install dependencies:

```bash
pip install -r requirments.txt
playwright install
```

---

## Usage

```bash
python main.py
```

- Opens the LinkedIn Zip game page.
- Waits for the **Start Game** button.
- Clicks the button and waits for the game grid to appear.
- Parses the grid, solves the puzzle, and displays the solution.

---

## Project Structure

```
.
├── game
│   ├── Board.py          # Board class
│   ├── Cell.py           # Cell class
│   └── Constants.py      # Directions and helpers
├── solver
│   ├── Solver.py         # HTML parser and path solver
├── ui
│   └── BoardViewer.py    # Visualization of board and solution
├── main.py               # Entry point
└── README.md
```

---

## How it Works

1. **Playwright Automation**:  
   Opens the LinkedIn game page and navigates to the game iframe. Clicks the **Start Game** button automatically.

2. **HTML Parsing**:  
   Extracts the `.trail-grid` from the iframe using `BeautifulSoup`.

3. **Solver**:  
   Generates a solution path through the numbers in order.

4. **Visualization**:  
   Displays the solution path on the grid using `Matplotlib`.

---
## Solver Algorithm

The solver uses a **recursive backtracking approach** to find a path through the Zip game grid, visiting each numbered cell in order. Here’s how it works:

1. **Board Representation**  
   Each cell is represented by a `Cell` object, which may contain a number and borders (walls). The `Board` class provides methods to get all valid moves from a cell while respecting walls.

2. **Starting and Ending Points**  
   - The solver first identifies all numbered cells using `getNumsInds(board)`.  
   - The path starts from the first number and must end at the last number, visiting all numbers in order.

3. **Recursive Backtracking (`findPath`)**  
   - At each step, the function considers all valid moves from the current cell (`getAllMoves`).  
   - Moves are shuffled to explore the search space in a randomized order, which helps avoid deterministic dead-ends.  
   - If the current cell contains a number, it verifies that the number is **exactly 1 greater** than the last visited number.  
   - The current cell is added to the path and marked as visited.  
   - The function recursively explores all valid moves from the current cell.  
   - If a move leads to a solution (reaching the end with all cells visited), the path is returned.

4. **Backtracking**  
   - If a move does not lead to a solution, the algorithm backtracks: it removes the last cell from the path and explores alternative moves.  
   - This continues until a valid path covering the entire grid in number order is found.

5. **Solve Function (`solve`)**  
   - Initializes the visited set and identifies start and end positions.  
   - Calls `findPath` recursively to compute the path.  
   - Returns the final path as a list of `(row, column)` tuples, representing the order of cells to visit.

---

### ⚡ Key Points

- The solver respects walls and only moves where allowed.  
- Randomized move order reduces bias in traversal and helps find solutions faster in some cases.  
- Supports visualization via `displayBoard` for debugging or demonstration.

---

## Notes

- The LinkedIn Zip game loads inside an iframe, so it’s important to fetch the HTML from the iframe, not the main page.
- Make sure your Playwright browser session is **headless=False** for debugging.
- You can adjust timeouts in `frame.wait_for_selector()` if the game takes longer to load.

---

## Acknowledgements

- Inspired by the LinkedIn Zip game.
- Uses Playwright for automation and Matplotlib for visualization.

