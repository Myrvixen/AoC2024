with open("day22.txt") as f:
    nums = [int(x) for x in f.read().splitlines()]

steps = 2000
for _ in range(steps):
    for i, num in enumerate(nums):
        res = num * 64
        res = res ^ num
        res = res % 16777216
        
        res2 = int(res / 32)
        res2 = res2 ^ res
        res2 = res2 % 16777216

        res3 = res2 * 2048
        res3 = res3 ^ res2
        res3 = res3 % 16777216

        nums[i] = res3

#print(nums)
print("Part 1:", sum(nums))
