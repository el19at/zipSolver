from playwright.sync_api import sync_playwright
from solver.Solver import html_to_board, solve
from ui.BoardViewer import BoardViewer
import time

def main():
    url = "https://www.linkedin.com/games/zip"

    with sync_playwright() as p:
        print('get the game board...')
        btnId = '#launch-footer-start-button'
        browser = p.chromium.launch(headless=True)  # False = see the browser
        page = browser.new_page()
        page.goto(url)
        iframe_element = page.wait_for_selector("iframe.game-launch-page__iframe")
        frame = iframe_element.content_frame()  # switch to iframe context

        # Wait for the Start Game button inside the iframe
        frame.wait_for_selector(btnId)
        frame.click(btnId)

        # Wait for the game grid inside the iframe
        frame.wait_for_selector(".trail-grid")
        htmlTxt = frame.content()
        browser.close()

    # Build board and solve
    print('build board')
    board = html_to_board(htmlTxt)
    start = time.time()
    print('solving...(be patient)')
    path = solve(board)
    end = time.time()
    print(f"solved in: {end - start:.6f} seconds")

    bv = BoardViewer(board, path)
    bv.show()

if __name__ == '__main__':
    main()
