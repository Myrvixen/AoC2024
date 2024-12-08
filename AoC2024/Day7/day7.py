def DFS(numbers, target, operation='+', total=0, part2=False):

    if total > target:
        return False

    if len(numbers) == 0:
        return total == target

    if operation == '+':
        new_total = total + numbers[0]
    elif operation == '*':
        new_total = total * numbers[0]
    elif operation == '||' and part2:
        new_total = int(str(total) + str(numbers[0]))
    else:
        raise ValueError(f"Wrong operation: '{operation}'")

    ops = ['+', '*'] + ['||']*part2
    for op in ops:
        if DFS(numbers[1:], target, op, new_total, part2):
            return True
    return False


with open("day7.txt") as f:
    lines = f.read().splitlines()

calibration_result1 = calibration_result2 = 0
for line in lines:
    words = line.split()
    result = int(words[0][:-1])
    numbers = [int(x) for x in words[1:]]

    success = DFS(numbers.copy(), result)

    if success:
        calibration_result1 += result
        calibration_result2 += result
    else:
        if DFS(numbers.copy(), result, part2=True):
            calibration_result2 += result
    

print("Part 1:", calibration_result1)
print("Part 2:", calibration_result2)