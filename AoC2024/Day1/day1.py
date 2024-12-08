import numpy as np

with open("day1.txt") as f:
    nums = np.array([line.split() for line in f.readlines()]).astype(int)

sorted = np.sort(nums, axis=0)
sol1 = np.sum(np.abs(np.diff(sorted, axis=1)))
print("Part 1:", sol1)

left_dict = {e: 0 for e in np.unique(sorted[:, 0])}
for e in sorted[:, 1]:
    if e in left_dict:
        left_dict[e] += 1

sol2 = 0
for e, val in left_dict.items():
    sol2 += e*val

print("Part 2:", sol2)