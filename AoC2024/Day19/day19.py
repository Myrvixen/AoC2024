import regex as re

with open("test.txt") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = set(patterns.split(", "))
    designs = designs.splitlines()

p = "(^(?:" + "|".join(patterns) + ")*$)"
valid = 0
for design in designs:
    matches = re.findall(p, design, overlapped=True)
    if len(matches) > 0:
        valid += 1


print("Part 1:", valid)
