import sys
from collections import deque
from itertools import permutations, combinations

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
            return []
        x, y, d = node
        path.append(d)
    return list(reversed(path))


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


def is_stackable(stack, total_steps):
    total_weight = 0
    for w, d in reversed(stack):  # 下から順に
        if d < total_weight * total_steps:
            return False
        total_weight += w
    return True


def find_unvisited_boxes(n, carried):
    return [(i, j) for i in range(n) for j in range(n) if not carried[i][j] and (i, j) != (0, 0)]


def try_transport_group(n, w, d, carried, group):
    best_order = None
    best_path = None
    best_total_steps = None

    for perm in permutations(group):
        current = (0, 0)
        path = []
        stack = []
        total_steps = 0

        for pos in perm:
            subpath = bfs_path(n, current, pos)
            if not subpath:
                break
            path += subpath
            total_steps += len(subpath)
            stack.append((w[pos[0]][pos[1]], d[pos[0]][pos[1]]))
            current = pos
        else:
            backpath = bfs_path(n, current, (0, 0))
            if not backpath:
                continue
            total_steps += len(backpath)
            if is_stackable(stack, total_steps):
                best_order = perm
                best_path = path + backpath
                best_total_steps = total_steps
                break  # 採用

    if best_order is not None:
        for move in best_path[:-(len(best_path) - len(path))]:
            print(move)
        print("1\n" * len(best_order), end="")
        for move in best_path[-(best_total_steps - len(path)):]:
            print(move)
        for i, j in best_order:
            carried[i][j] = True
        return True
    return False


def transport_boxes_grouped(n, w, d):
    carried = [[False] * n for _ in range(n)]

    while True:
        boxes = find_unvisited_boxes(n, carried)
        if not boxes:
            break

        success = False
        # 3個→2個→1個の順に試す
        for group_size in [3, 2, 1]:
            for group in combinations(boxes, group_size):
                if try_transport_group(n, w, d, carried, group):
                    success = True
                    break
            if success:
                break

        # 運べる箱がない（全部WAになりそう）場合は終了
        if not success:
            break


def main():
    """
    Main function to read input and run the box transport logic.
    """
    n, w, d = read_input()
    transport_boxes_grouped(n, w, d)


if __name__ == "__main__":
    main()
