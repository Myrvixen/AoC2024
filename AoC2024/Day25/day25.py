import numpy as np

with open("day25.txt") as f:
    schematics = f.read().split("\n\n")

keys, locks = set(), set()
for s in schematics:
    grid = np.array([list(line) for line in s.splitlines()])
    pins = np.sum(grid == "#", axis=0) - 1

    if np.all([grid[0] == "#"]):
        locks.add(tuple(pins))
    else:
        keys.add(tuple(pins))

valid_pairs = 0
for key in keys:
    for lock in locks:
        #print(lock, key, [(lock[i] + key[i]) <= 5 for i in range(len(lock))])
        valid_pairs += all([(lock[i] + key[i]) <= 5 for i in range(len(lock))])

print("Part 1:", valid_pairs)