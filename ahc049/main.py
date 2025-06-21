import sys
input = sys.stdin.read

data = input().split('\n')
grid = [list(map(int, line.split())) for line in data if line.strip()]
h, w = grid[0][0], 20
grid = grid[1:h+1]

path = []
x, y = 0, 0
for i in range(1, len(grid)):
    if grid[i][y] == grid[i-1][y]:
        path.append('D')
    elif grid[i][y] > grid[i-1][y]:
        path.append('R')
    elif grid[i][y] < grid[i-1][y]:
        path.append('L')
    else:
        path.append('U')
print('\n'.join(path))
