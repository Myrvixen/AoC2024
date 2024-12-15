with open("day11.txt") as f:
    stones = [int(x) for x in f.read().strip().split()]

num_blinks = 25

for _ in range(num_blinks):
    offset = 0
    new_stones = stones.copy()
    for i, stone in enumerate(stones):
        if stone == 0:
            new_stones[i+offset] = 1
        elif (length := len(stone_str := str(stone))) % 2 == 0:
            left, right = stone_str[:length//2], stone_str[length//2:]
            new_stones[i+offset] = int(left)
            new_stones.insert(i+1+offset, int(right))
            offset += 1
        else:
            new_stones[i+offset] *= 2024
    stones = new_stones

print("Part 1:", len(stones))