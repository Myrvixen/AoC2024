#with open("test.txt") as f:
with open("day4.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

m, n = len(grid), len(grid[0])
dirs = [(dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if not dx == dy == 0]

count1 = count2 = 0
for i in range(m):
    for j in range(n):
        
        if grid[i][j] == 'X':
            for dy, dx in dirs:
                if 0 <= i + 3*dy < m and 0 <= j + 3*dx < n:
                    word = ''.join([grid[i + k*dy][j + k*dx] for k in range(0, 4)])
                    if word == "XMAS":
                        count1 += 1
        
        if grid[i][j] ==  'A':
            if 0 < i < m-1 and 0 < j < n-1:
                diag1 = ''.join([grid[i-1][j-1], grid[i][j], grid[i+1][j+1]])
                diag2 = ''.join([grid[i+1][j-1], grid[i][j], grid[i-1][j+1]])
                if "MAS" in (diag1, diag1[::-1]) and "MAS" in (diag2, diag2[::-1]):
                    count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)