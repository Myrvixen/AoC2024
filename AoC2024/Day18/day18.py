import numpy as np

positions = np.loadtxt("day18.txt", delimiter=",").astype(int)[:, ::-1]
m, n = 71, 71
num_bytes = 1024
end = (70, 70)
#m, n = 7, 7
#num_bytes = 12
#end = (6, 6)
start = (0, 0)
dirs = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])

grid = np.ones((m, n), dtype=bool)
grid[positions[:num_bytes, 0], positions[:num_bytes, 1]] = 0


def dijkstra(start, end):
    
    Q = {tuple(pos): np.inf for pos in np.argwhere(grid)}
    Q[tuple(start)] = 0
    dists = {}

    while len(Q) > 0:
        u = min(Q, key=Q.get)
        dist_u = Q.pop(u)
        dists[u] = dist_u

        if u == end:
            break

        for d in dirs:
            v = tuple(u + d)
            if v in Q and grid[v] and 0 <= v[0] < m and 0 <= v[1] < n:
                new_dist = dist_u + 1
                if new_dist < Q[v]:
                    Q[v] = new_dist
 
    return dists[end]

sol1 = dijkstra(start, end)
print("Part 1:", sol1)
        

