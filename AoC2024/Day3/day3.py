import re

with open("day3.txt") as f:
    text = f.read()

pattern = "(do\(\)|don't\(\))|(?:mul\((\d+),(\d+)\))"
matches = re.findall(pattern, text)

tot = tot2 = 0
enabled = True
for match in matches:
    if match[0] == "do()":
        enabled = True
    elif match[0] == "don't()":
        enabled = False
    else:
        tot += int(match[1]) * int(match[2])
        if enabled:
            tot2 += int(match[1]) * int(match[2])

print("Part 1:", tot)
print("Part 2:", tot2)