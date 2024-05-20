import random
import time


def get_random_cell(rows, cols) -> (int, int):
    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    return row, col


def generate_graph(rows: int, cols: int, alpha: float, seed=None) -> list[list[int]]:
    if seed is not None:
        random.seed(seed)
    graph: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
    for _ in range(int(alpha * rows * cols)):
        row, col = get_random_cell(rows, cols)
        graph[row][col] = 1
    random.seed(time.time())

    return graph
