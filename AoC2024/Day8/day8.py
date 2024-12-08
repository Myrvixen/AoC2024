import numpy as np

with open("day8.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()])

m, n = grid.shape
antennas = {c: np.argwhere(grid == c) for c in np.unique(grid) if c != '.'}

antinodes1 = set()
antinodes2 = set()
for ant in antennas:
    positions = antennas[ant]
    for i in range(len(positions)-1):
        for j in range(i+1, len(positions)):
            diff = positions[j] - positions[i]
            node1 = positions[i] + 2*diff
            node2 = positions[i] - diff
            if 0 <= node1[0] < m and 0 <= node1[1] < n:
                antinodes1.add(tuple(node1))
            if 0 <= node2[0] < m and 0 <= node2[1] < n:
                antinodes1.add(tuple(node2))
            
            # Look in both directions and add all nodes within bounds
            direction = (diff / np.gcd.reduce(diff)).astype(int)
            node = positions[i].copy()
            while 0 <= node[0] < m and 0 <= node[1] < n:
                antinodes2.add(tuple(node))
                node -= direction
            
            node = positions[i].copy()
            while 0 <= node[0] < m and 0 <= node[1] < n:
                antinodes2.add(tuple(node))
                node += direction

print("Part 1:", len(antinodes1))
print("Part 2:", len(antinodes2))