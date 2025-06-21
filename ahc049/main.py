import sys
from collections import deque

sys.setrecursionlimit(10_000)

DIRECTIONS = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]

def read_input():
    """
    Reads input from standard input.

    The input format is:
    - An integer n representing the grid size.
    - Two n x n integer matrices w and d (currently only n is returned).

    Returns:
        int: The size n of the grid.
    """
    n = int(input())
    w = [list(map(int, input().split())) for _ in range(n)]
    d = [list(map(int, input().split())) for _ in range(n)]
    return n

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

    path = []
    x, y = goal
    while (x, y) != start:
        x, y, d = prev[x][y]
        path.append(d)
    return reversed(path)

def print_path(path):
    """
    Prints each direction in the path on a new line.

    Args:
        path (iterator): Iterator or list of directions ('U', 'D', 'L', 'R').
    """
    print('\n'.join(path))

def transport_boxes(n):
    """
    For each cell in the n x n grid (except the start), finds and prints:
    - The path from start (0, 0) to the cell.
    - A '1' indicating picking up a box.
    - The path back from the cell to start (0, 0).

    Args:
        n (int): Size of the grid.
    """
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            path_there = bfs_path(n, (0, 0), (i, j))
            print_path(path_there)
            print('1')  # pick up
            path_back = bfs_path(n, (i, j), (0, 0))
            print_path(path_back)

def main():
    """
    Main function to read input and run the box transport logic.
    """
    n = read_input()
    transport_boxes(n)

if __name__ == '__main__':
    main()
