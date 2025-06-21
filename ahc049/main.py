import sys
from collections import deque
from itertools import product

sys.setrecursionlimit(10_000)

DIRECTIONS = [("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)]


def read_input():
    """
    Reads input from standard input.

    The input format is:
    - An integer n representing the grid size.
    - Two n x n integer matrices w and d.

    Returns:
        int: The size n of the grid.
        list[list[int]]: Weight matrix w.
        list[list[int]]: Strenght matrix d.
    """
    n = int(input())
    w = [list(map(int, input().split())) for _ in range(n)]
    d = [list(map(int, input().split())) for _ in range(n)]
    return (n, w, d)


def bfs_search(n, start, goal):
    """
    Performs BFS to find a path from start to goal on an n x n grid.

    Args:
        n (int): Size of the grid (n x n).
        start (tuple): Starting coordinates (x, y).
        goal (tuple): Goal coordinates (x, y).

    Returns:
        list[list[tuple]]: A 2D list representing the previous cell and direction taken to reach each cell.
    """
    visited = [[False] * n for _ in range(n)]
    prev = [[None] * n for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break
        for direction, dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                prev[nx][ny] = (x, y, direction)
                queue.append((nx, ny))

    return prev


def reconstruct_path(start, goal, prev):
    """
    Reconstructs the path from start to goal using the 'prev' table.

    Args:
        start (tuple): Starting coordinates (x, y).
        goal (tuple): Goal coordinates (x, y).
        prev (list[list[tuple]]): A 2D list of previous nodes and directions.

    Returns:
        iterator: An iterator of directions ('U', 'D', 'L', 'R') from start to goal.
    """
    path = []
    x, y = goal
    while (x, y) != start:
        node = prev[x][y]
        if node is None:
            return iter([])  # No path found
        x, y, d = node
        path.append(d)
    return reversed(path)


def bfs_path(n, start, goal):
    """
    Finds the shortest path from start to goal on an n x n grid using BFS.

    Args:
        n (int): Size of the grid (n x n).
        start (tuple): Starting coordinates (x, y).
        goal (tuple): Goal coordinates (x, y).

    Returns:
        iterator: An iterator of directions ('U', 'D', 'L', 'R') from start to goal.
    """
    prev = bfs_search(n, start, goal)
    return reconstruct_path(start, goal, prev)


def print_path(path):
    """
    Prints each direction in the path on a new line.

    Args:
        path (iterator): Iterator or list of directions ('U', 'D', 'L', 'R').
    """
    print("\n".join(path))


def transport_boxes(n, w, d):
    """
    For each cell in the n x n grid (except the start), finds and prints:
    - The path from start (0, 0) to the cell.
    - A '1' indicating picking up a box.
    - The path back from the cell to start (0, 0).

    Args:
        n (int): Size of the grid.
        w (list[list[int]]): Weight matrix.
        d (list[list[int]]): Strength matrix.
    """
    for i, j in product(range(n), repeat=2):
        if i == 0 and j == 0:
            continue
        path_there = bfs_path(n, (0, 0), (i, j))
        print_path(path_there)
        print("1")  # pick up
        path_back = bfs_path(n, (i, j), (0, 0))
        print_path(path_back)


def main():
    """
    Main function to read input and run the box transport logic.
    """
    n, w, d = read_input()
    transport_boxes(n, w, d)


if __name__ == "__main__":
    main()
