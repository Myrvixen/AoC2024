def is_valid(update):
    for i in range(len(update)-1):
        num1 = update[i]
        for j in range(i+1, len(update)):
            num2 = update[j]
            if f"{num2}|{num1}" in orderings:
                return False
    return True

def reorder(update):
    i = 0
    while not is_valid(update):
        for i in range(len(update)-1):
            num1 = update[i]
            for j in range(i+1, len(update)):
                num2 = update[j]
                if f"{num2}|{num1}" in orderings:
                    update[i] = num2
                    update[j] = num1
                    break


with open("day5.txt") as f:
    orderings, updates = f.read().split("\n\n")
    orderings = set([line for line in orderings.split("\n")])
    updates = [[int(x) for x in line.split(",")] for line in updates.strip().split("\n")]

sum1 = sum2 = 0
for update in updates:
    if is_valid(update):
        sum1 += update[len(update)//2]
    else:
        reorder(update)
        sum2 += update[len(update)//2]

print("Part 1:", sum1)
print("Part 2:", sum2)