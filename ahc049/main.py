import sys
from collections import deque

sys.setrecursionlimit(10_000)

DIRECTIONS = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]

def read_input():
    n = int(input())
    w = [list(map(int, input().split())) for _ in range(n)]
    d = [list(map(int, input().split())) for _ in range(n)]
    return n

def bfs_path(n, start, goal):
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
    print('\n'.join(path))

def transport_boxes(n):
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
    n = read_input()
    transport_boxes(n)

if __name__ == '__main__':
    main()
