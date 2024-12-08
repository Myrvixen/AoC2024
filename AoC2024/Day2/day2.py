import numpy as np

#with open("test.txt") as f:
with open("day2.txt") as f:
    reports = [list(map(int, line.split())) for line in f.readlines()]


def is_safe(report):
    diffs = [y - x for x, y in zip(report, report[1:])]
    return all([1 <= x <= 3 for x in diffs]) or all([-1 >= x >= -3 for x in diffs])

safe = damp_safe = 0
for report in reports:
    safe += int(is_safe(report))
    
    if any([is_safe(report[:i] + report[i+1:]) for i in range(len(report))]):
        damp_safe += 1


print("Part 1:", safe)
print("Part 2:", damp_safe)