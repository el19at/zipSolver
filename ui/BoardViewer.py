from game.Board import Board

import matplotlib.pyplot as plt
import matplotlib.patches as patches

class BoardViewer:
    def __init__(self, board: Board, path: list[tuple[int, int]] = None):
        self.board = board
        self.path = path if path is not None else []

    def show(self):
        dim = self.board.dimension
        fig, ax = plt.subplots(figsize=(dim, dim))

        # Draw cells
        for i in range(dim):
            for j in range(dim):
                cell = self.board.grid[i][j]
                rect = patches.Rectangle(
                    (j, dim - 1 - i), 1, 1, fill=False, linewidth=1, edgecolor="black"
                )
                ax.add_patch(rect)

                # Draw number (if exists)
                if cell.value != 0:
                    ax.text(
                        j + 0.5,
                        dim - 1 - i + 0.5,
                        str(cell.value),
                        ha="center",
                        va="center",
                        fontsize=14,
                        fontweight="bold",
                        color="blue",
                    )

                # Draw borders (thick walls)
                x, y = j, dim - 1 - i
                for d in cell.borders:
                    if d == (-1, 0):  # UP
                        ax.plot([x, x + 1], [y + 1, y + 1], color="red", linewidth=3)
                    if d == (1, 0):  # DOWN
                        ax.plot([x, x + 1], [y, y], color="red", linewidth=3)
                    if d == (0, -1):  # LEFT
                        ax.plot([x, x], [y, y + 1], color="red", linewidth=3)
                    if d == (0, 1):  # RIGHT
                        ax.plot([x + 1, x + 1], [y, y + 1], color="red", linewidth=3)

        # Draw path (if provided)
        if self.path:
            xs, ys = [], []
            for (i, j) in self.path:
                xs.append(j + 0.5)          # center x
                ys.append(dim - 1 - i + 0.5)  # center y (flipped vertically)
            ax.plot(xs, ys, color="green", linewidth=2, marker="o")

        # Set limits & remove ticks
        ax.set_xlim(0, dim)
        ax.set_ylim(0, dim)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal")
        plt.show()
