import numpy as np

with open("day6.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()], dtype=str)

m, n = len(grid), len(grid[0])
pos = np.argwhere(grid == '^')[0]

dir = np.array([-1, 0])
R = np.array([[0, 1], [-1, 0]])  # Rotation matrix 90 deg clockwise

visited = {tuple(pos): set([tuple(dir)])}
steps = num_loops = 0
while True:
    new_pos = tuple(pos + dir)
    if not(0 <= new_pos[0] < m and 0 <= new_pos[1] < n):
        break
    
    if grid[new_pos] == "#":
        new_pos = pos
        dir = R @ dir
    else:
        # search for loops
        # TODO: Answer too low, probably missing new loops created by multiple bumps
        dir_90 = R @ dir
        dir_180 = R @ dir_90
        loop_pos = tuple(pos + dir_90)
        while 0 <= loop_pos[0] < m and 0 <= loop_pos[1] < n and grid[loop_pos] != "#":
 
            if loop_pos in visited and tuple(dir_180) in visited[loop_pos] \
                and grid[tuple(loop_pos + dir_90)] == "#":
            
                num_loops += 1
                #print("Found loop with obstruction at", new_pos)
                break
            loop_pos = tuple(loop_pos + dir_90)
            
    if new_pos in visited:
        visited[new_pos].add(tuple(dir))
    else:
        visited[new_pos] = set([tuple(dir)])
    
    pos = new_pos

print("Part 1:", len(visited))
print("Part 2:", num_loops)