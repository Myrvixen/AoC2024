import numpy as np

with open("day6.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()], dtype=str)

m, n = len(grid), len(grid[0])
pos = np.argwhere(grid == '^')[0]

dir = np.array([-1, 0])
R = np.array([[0, 1], [-1, 0]])  # Rotation matrix 90 deg clockwise

visited = {tuple(pos)}
steps = 0
while True:
    new_pos = tuple(pos + dir)
    if not(0 <= new_pos[0] < m and 0 <= new_pos[1] < n):
        break

    if grid[new_pos] == "#":
        new_pos = pos
        dir = R @ dir
    visited.add(new_pos)
    pos = new_pos

print("Part 1:", len(visited))
