import numpy as np

with open("test.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()], dtype=str)

m, n = grid.shape
start = np.argwhere(grid == "S")[0]
end = np.argwhere(grid == "E")[0]
dirs = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])

vertices = []
for space in np.argwhere(grid == "."):
    neighbors = (space + dirs)
    empty_neighbors = grid[neighbors[:,0], neighbors[:,1]] == "."
    if empty_neighbors.sum() >= 3:
        vertices.append(space)
    elif empty_neighbors.sum() == 2 and not (np.all(empty_neighbors[:2]) or np.all(empty_neighbors[2:])):
        vertices.append(space)

vertices = np.array(vertices)

edges = {tuple(v): set() for v in vertices}
for i in range(len(edges)):
    v = vertices[i]
    for j in range(i+1, len(vertices)):
        u = vertices[j]
        if 0 in v-u and np.all(grid[v[0]: u[0]+1, v[1]: u[1]+1] == "."):
            edges[tuple(v)].add(tuple(u))
            edges[tuple(u)].add(tuple(v))


def DFS(v, edges, target, dir_, total_dist, path):

    if v == target:
        return total_dist
    
    total_dists = []
    for u in edges:
        if u in path:
            continue

        print(u, v)
        move = np.array(u) - v
        new_dir = move/np.max(np.abs(move))
        move_cost = 0
        if np.array_equal(new_dir*(-1), dir_):
            continue
        elif not np.array_equal(new_dir, dir_):
            move_cost += 1000
        
        move_cost += np.sum(np.abs(move))
        total_dists.append(DFS(u, edges, target, new_dir, total_dist+move_cost, path+[u]))
    
    if len(total_dists) == 0:
        return np.inf
    return np.min(total_dists)


min_distance = DFS(tuple(start), edges, tuple(end), np.array([0, 1]), np.inf, [])
print(min_distance)


def dijkstra(edges, source, target):
    
    Q = set()
    dists = {}
    for v in edges:
        dists[v] = np.inf
        Q.add(v)
    dists[source] = 0
    direction = np.array([0, 1])

    while len(Q) > 0:
        v = min(dists, key=dists.get)
        Q.remove(v)

        for u in edges[v]:
            if u not in Q:
                continue
            dist_vec = np.array(u) - v
            #if dist_vec*(-1) 

            #dist = dists[v] + 

    


# grid[vertices[:, 0], vertices[:, 1]] = "x"
# for line in grid:
#     print(''.join(line))