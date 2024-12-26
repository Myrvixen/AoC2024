import numpy as np

with open("test.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()])

start = np.argwhere(grid == "S")[0]
end = np.argwhere(grid == "E")[0]

m, n = grid.shape
dirs = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
reachable_cheat = np.array([[i, j] for i in range(-3, 4) for j in range(-3, 4) if (abs(i) + abs(j)) in (2, 3)])
cheat_paths = {}


Q = set([tuple(start)])
dists = {tuple(start): 0}

while len(Q) > 0:
    pos = Q.pop()
    cheat_paths[tuple(pos)] = set()

    for d in dirs:
        pos_new = pos + d
        if 0 <= pos_new[0] < m and 0 <= pos_new[1] < m \
            and tuple(pos_new) not in dists:
            if not grid[tuple(pos_new)] == "#":
                Q.add(tuple(pos_new))
                dists[tuple(pos_new)] = dists[tuple(pos)] + 1
            else:
                for d_cheat in reachable_cheat:
                    pos_cheat = pos + d_cheat
                    if 0 <= pos_cheat[0] < m and 0 <= pos_cheat[1] < n \
                        and tuple(pos_cheat) not in dists and not grid[tuple(pos_cheat)] == "#":
                        cheat_paths[tuple(pos)].add(tuple(pos_cheat))


for pos, paths in cheat_paths.items():
    for pos_cheat in paths:
        print(dists[pos], dists[pos_cheat], dists[pos_cheat] - dists[pos])

#print(dists)
#print(dists[tuple(end)])

#print(cheat_paths)
