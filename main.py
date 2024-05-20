import random
import time

from colorama import Fore
from SearchAlgorithm import a_search_algorithm
from functions import generate_graph, get_random_cell

N, M = 300, 300
ALPHA = 1 / 4


def get_index(row: int, col: int) -> int:
    """
    :param row: номер строки
    :param col: номер столбца
    :return: индекс в графе
    """
    global N, M
    return row * M + col


def rev_get_index(idx: int) -> (int, int):
    """
    :param idx: индекс в графе
    :return: номер строки и столбца
    """
    global N, M
    return idx // M, idx % M


def is_correct_cell(row: int, col: int) -> bool:
    global N, M
    return (0 <= row < N) and (0 <= col < M) and GRAPH[row][col] != 1


def add_edges(row: int, col: int, _graph: list[list[(int, int)]]):
    idx = get_index(row, col)
    if is_correct_cell(row - 1, col):
        _graph[idx].append((get_index(row - 1, col), 1))
    if is_correct_cell(row + 1, col):
        _graph[idx].append((get_index(row + 1, col), 1))
    if is_correct_cell(row, col - 1):
        _graph[idx].append((get_index(row, col - 1), 1))
    if is_correct_cell(row, col + 1):
        _graph[idx].append((get_index(row, col + 1), 1))


def build_graph(g: list[list[int]]) -> list[list[(int, int)]]:
    global N, M
    _graph: list[list[(int, int)]] = [[] for _ in range(N * M)]

    for row in range(N):
        for col in range(M):
            if g[row][col] == 1:
                continue
            add_edges(row, col, _graph)

    return _graph


def build_vertex_coord() -> list[(int, int)]:
    global N, M
    vertex_coord: list[(int, int)] = [(-1, -1) for _ in range(N * M)]

    for row in range(N):
        for col in range(M):
            vertex_coord[get_index(row, col)] = (row, col)

    return vertex_coord


VERTEX_COORD = build_vertex_coord()


def print_used_cells(used_vertex: list[bool], path: list[int]):
    used_matrix: list[list[int]] = [[0 for _ in range(M)] for _ in range(N)]

    for v in range(N * M):
        row, col = rev_get_index(v)
        if used_vertex[v]:
            used_matrix[row][col] = 1

    for v in path:
        row, col = rev_get_index(v)
        used_matrix[row][col] = 2

    for row in range(N):
        for col in range(M):

            color = Fore.RED
            if used_matrix[row][col] == 1:
                color = Fore.GREEN
            elif used_matrix[row][col] == 2:
                color = Fore.BLUE
            print(color + "#" + Fore.WHITE, end="")
        print()
    print()


def print_board(board: list[list[int]], s: int, t: int):
    for row in range(N):
        for col in range(M):
            color = Fore.WHITE
            if (row, col) == rev_get_index(s) or (row, col) == rev_get_index(t):
                color = Fore.GREEN
            elif board[row][col] == 1:
                color = Fore.BLUE
            print(color + str(board[row][col]) + Fore.WHITE, end="")
        print()
    print()


def generate_start_and_finish(seed=None) -> (int, int):
    if seed is not None:
        random.seed(seed)

    s_r, s_c = get_random_cell(rows=N, cols=M)
    while GRAPH[s_r][s_c] == 1:
        s_r, s_c = get_random_cell(rows=N, cols=M)

    t_r, t_c = get_random_cell(rows=N, cols=M)
    while GRAPH[t_r][t_c] == 1:
        t_r, t_c = get_random_cell(rows=N, cols=M)

    random.seed(time.time())

    return get_index(s_r, s_c), get_index(t_r, t_c)


if __name__ == "__main__":
    seed: int = 778

    GRAPH = generate_graph(N, M, ALPHA, seed)

    graph = build_graph(GRAPH)

    s, t = generate_start_and_finish(seed)

    print(s, t)

    print_board(GRAPH, s, t)

    dist, path, all_used_vertex = a_search_algorithm(graph=graph, s=s, t=t)

    print_used_cells(all_used_vertex, path)

    print(dist)
