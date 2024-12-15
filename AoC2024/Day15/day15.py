import numpy as np

def move_recursive(pos, dir_, grid):
    new_pos = pos + dir_
    if grid[tuple(new_pos)] == "#":
        return pos
    elif grid[tuple(new_pos)] == "O" and np.array_equal(move_recursive(new_pos, dir_, grid), new_pos):
        return pos
    
    grid[tuple(new_pos)] = grid[tuple(pos)]
    grid[tuple(pos)] = "."
    return new_pos


def move_recursive2(pos, dir_, grid):
    new_pos = pos + dir_
    if grid[tuple(new_pos)] == "#":
        print(1)
        return pos
    elif (half := grid[tuple(new_pos)]) in ("[", "]"):
        if dir_[0] == 0 and np.array_equal(move_recursive2(new_pos, dir_, grid), new_pos):
            print(2)
            return pos
        
        other_pos = new_pos + [0, -1] if half == "]" else new_pos + [0, 1]
        if np.array_equal(move_recursive2(new_pos, dir_, grid), move_recursive2(other_pos, dir_, grid)):
            grid[tuple(new_pos)] = grid[tuple(pos)]
            grid[tuple(other_pos)] = grid[tuple(other_pos - dir_)]
            grid[tuple(pos)] = "."
            grid[tuple(other_pos - dir_)] = "."
            print(3)
            return new_pos
        else:
            print(4)
            return pos
    
    grid[tuple(new_pos)] = grid[tuple(pos)]
    grid[tuple(pos)] = "."
    print(5, pos, new_pos, dir_)
    return new_pos


    

with open("test.txt") as f:
    grid, moves = f.read().split("\n\n")
    wide_grid = grid.replace("#", "##")
    wide_grid = wide_grid.replace("O", "[]")
    wide_grid = wide_grid.replace(".", "..")
    wide_grid = wide_grid.replace("@", "@.")
    grid = np.array([list(line) for line in grid.splitlines()])
    wide_grid = np.array([list(line) for line in wide_grid.splitlines()])
    moves = moves.replace("\n", "")

move_to_dir = {"v": np.array([1, 0]), "^": np.array([-1, 0]), 
               "<": np.array([0, -1]), ">": np.array([0, 1])}

pos = np.argwhere(grid == "@")[0]
wide_pos = np.argwhere(wide_grid == "@")[0]


for move in moves:
    dir_ = move_to_dir[move]

    pos = move_recursive(pos, dir_, grid)
    wide_pos = move_recursive2(wide_pos, dir_, wide_grid)

    print(f"Move {move}:")
    for line in wide_grid:
        print(''.join(line))
    print()

for line in wide_grid:
    print(''.join(line))

sum_GPS = np.sum(np.argwhere(grid == "O") * np.array([100, 1]))
print("Part 1:", sum_GPS)
