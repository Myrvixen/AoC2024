import numpy as np

def region_perimeter(pos, plant_type, region):

    if not (0 <= pos[0] < m and 0 <= pos[1] < n) or grid[tuple(pos)] != plant_type:
        return 1

    if tuple(pos) in region:
        return 0

    region.add(tuple(pos))
    num_fences = 0
    for dir in np.array([[-1, 0], [1, 0], [0, -1], [0, 1]]):
        num_fences += region_perimeter(pos + dir, plant_type, region)
    return num_fences


with open("day12.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()], dtype=str)

m, n = grid.shape
visited = set()
tot_price = 0

for i in range(m):
    for j in range(n):
        if (i, j) not in visited:
            region = set()
            perimeter = region_perimeter((i, j), grid[i, j], region)
            area = len(region)
            price = perimeter * area
            tot_price += perimeter * area
            visited.update(region)

            #print(grid[i,j], region, price, perimeter, area)


print("Part 1: ", tot_price)

