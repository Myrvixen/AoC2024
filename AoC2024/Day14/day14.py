import re
import numpy as np

with open("day14.txt") as f:
    robots = f.read()

#m, n = 7, 11  # test.txt
m, n = 103, 101  # day14.txt
timesteps = 100
quadrant_count = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
pattern = "p=(\-*\d+),(\-*\d+) v=(\-*\d+),(\-*\d+)"
for x, y, vx, vy in re.findall(pattern, robots):
    pos = np.array([y, x], dtype=int)
    vel = np.array([vy, vx], dtype=int)
    
    final_pos = (pos + vel*timesteps) % np.array([m, n])
    if final_pos[0] == m//2 or final_pos[1] == n//2:
        continue
    quadrant_count[(final_pos[0] > m//2, final_pos[1] > n//2)] += 1
                
safety_factor = np.prod(list(quadrant_count.values()))
print("Part 1:", safety_factor)