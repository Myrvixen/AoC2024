import numpy as np

def DFS(pos, tops_visited, part1=True):

    if grid[tuple(pos)] == 9:
        if not part1:
            return 1
        if part1 and tuple(pos) not in tops_visited:
            tops_visited.add(tuple(pos))
            return 1
    
    num_trails = 0
    for dir in dirs:
        new_pos = pos + dir
        if 0 <= new_pos[0] < m and 0 <= new_pos[1] < n and grid[tuple(new_pos)] - grid[tuple(pos)] == 1:
            num_trails += DFS(new_pos, tops_visited, part1)
    return num_trails

with open("day10.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()]).astype(int)

m, n = grid.shape
trailheads = np.argwhere(grid == 0)
dirs = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])

total_hikes = sum([DFS(t, set()) for t in trailheads])
total_ratings = sum([DFS(t, set(), False) for t in trailheads])
print("Part 1:", total_hikes)
print("Part 2:", total_ratings)
