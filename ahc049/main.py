import sys
from collections import deque

sys.setrecursionlimit(10000)

# 入力読み込み
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
D = [list(map(int, input().split())) for _ in range(N)]

# 移動用
DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
DIR_CHARS = ["U", "D", "L", "R"]


def bfs_path(sx, sy, gx, gy):
    """幅優先探索で入口からの最短経路を求める"""
    visited = [[False] * N for _ in range(N)]
    prev = [[None] * N for _ in range(N)]
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == (gx, gy):
            break
        for d, (dx, dy) in zip(DIR_CHARS, DIRS.values()):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                prev[nx][ny] = (x, y, d)
                queue.append((nx, ny))

    # 経路復元
    path = []
    cx, cy = gx, gy
    while (cx, cy) != (sx, sy):
        px, py, dir_char = prev[cx][cy]
        path.append(dir_char)
        cx, cy = px, py
    return path[::-1]


def move_path(path):
    for step in path:
        print(step)


# 各マスに対して、距離の近い順に運び出す
for i in range(N):
    for j in range(N):
        if (i, j) == (0, 0):
            continue
        path_to_box = bfs_path(0, 0, i, j)
        move_path(path_to_box)
        print("1")  # pick
        path_back = bfs_path(i, j, 0, 0)
        move_path(path_back)
        # 運んだので箱を出す（実際はそのまま持って出たとみなす）
