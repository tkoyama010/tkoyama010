import sys
from collections import deque
from itertools import product

sys.setrecursionlimit(10_000)

DIRECTIONS = [("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)]


def read_input():
    """
    標準入力からデータを読み込む。

    入力形式:
    - グリッドのサイズを表す整数 n
    - 重さ行列 w を表す n 行の整数列
    - 耐久力行列 d を表す n 行の整数列

    戻り値:
        n (int): グリッドのサイズ
        w (list[list[int]]): 重さの行列
        d (list[list[int]]): 耐久力の行列
    """
    n = int(input())
    w = [list(map(int, input().split())) for _ in range(n)]
    d = [list(map(int, input().split())) for _ in range(n)]
    return (n, w, d)


def bfs_search(n, start, goal):
    """
    BFSアルゴリズムで start から goal までの最短経路を探索する。

    引数:
        n (int): グリッドのサイズ (n x n)
        start (tuple): 開始座標 (x, y)
        goal (tuple): 目標座標 (x, y)

    戻り値:
        prev (list[list[tuple or None]]): 各セルについて、(前のセルの x 座標, 前のセルの y 座標, 移動方向) を記録した2次元リスト
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
    prev リストを用いて start から goal までの移動方向の経路を復元する。

    引数:
        start (tuple): 開始座標 (x, y)
        goal (tuple): 目標座標 (x, y)
        prev (list[list[tuple or None]]): 各セルについての前のセルと移動方向を記録した2次元リスト

    戻り値:
        iterator: 移動方向の列（'U', 'D', 'L', 'R'）
    """
    path = []
    x, y = goal
    while (x, y) != start:
        node = prev[x][y]
        if node is None:
            return iter([])  # 経路が存在しない場合は空のイテレータを返す
        x, y, d = node
        path.append(d)
    return reversed(path)


def bfs_path(n, start, goal):
    """
    start から goal までの最短経路の移動方向列を返す。

    戻り値:
        iterator: 移動方向の列
    """
    prev = bfs_search(n, start, goal)
    return reconstruct_path(start, goal, prev)


def print_path(path):
    """
    移動方向の列を1行ずつ出力する。
    """
    print("\n".join(path))


def transport_boxes(n, w, d):
    """
    各セル（0,0は除く）について、箱が1個を運ぶことを試みる。
    その際、隣接する右のセルに箱がある場合は、そこに移動し、追加で箱を運ぶ。
    耐久力チェックを行い、条件を満たせば経路を出力する。

    引数:
       n (int): グリッドのサイズ
       w (list[list[int]]): 重さの行列
       d (list[list[int]]): 耐久力の行列
    """
    transport_two_boxes_count = 0
    is_transported = [[False] * n for _ in range(n)]
    for i, j in product(range(n - 1, -1, -1), repeat=2):
        if i == 0 and j == 0:
            continue

        if is_transported[i][j]:
            continue

        path_there = list(bfs_path(n, (0, 0), (i, j)))
        path_back = list(bfs_path(n, (i, j), (0, 0)))
        print_path(path_there)
        print(str(1))  # 段ボールを持つ
        print_path(path_back[0])
        direction = path_back[0]
        if direction == "U":
            k = i - 1
            l = j
        elif direction == "D":
            k = i + 1
            l = j
        elif direction == "L":
            k = i
            l = j - 1
        elif direction == "R":
            k = i
            l = j + 1
        total_damage = w[k][l] * len(path_back)
        if total_damage < d[i][j]:
            print("1")
            is_transported[k][l] = True
        print_path(path_back[1:])
        is_transported[i][j] = True


def main():
    n, w, d = read_input()
    transport_boxes(n, w, d)


if __name__ == "__main__":
    main()
