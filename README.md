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

```python main.py
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

## Notes

- The LinkedIn Zip game loads inside an iframe, so it’s important to fetch the HTML from the iframe, not the main page.
- Make sure your Playwright browser session is **headless=False** for debugging.
- You can adjust timeouts in `frame.wait_for_selector()` if the game takes longer to load.

---

## Acknowledgements

- Inspired by the LinkedIn Zip game.
- Uses Playwright for automation and Matplotlib for visualization.

