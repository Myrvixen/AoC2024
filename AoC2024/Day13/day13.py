import numpy as np
import re

def calculate_cost(xa, xb, ya, yb, X, Y, part2=False):
    if part2:
        X += 10000000000000
        Y += 10000000000000

    a, a_mod = divmod((yb*X - xb*Y), (xa*yb - xb*ya))
    b, b_mod = divmod((ya*X - xa*Y), (ya*xb - yb*xa))
    if a_mod != 0 or b_mod != 0:
        return 0

    return 3*a + b


with open("day13.txt") as f:
    machines = f.read().split("\n\n")

button_reg = "Button (?:A|B): X\+(\d+), Y\+(\d+)"
prize_reg = "Prize: X=(\d+), Y=(\d+)"

total_cost1 = total_cost2 = 0
for m in machines:
    
    (xa, ya), (xb, yb) = re.findall(button_reg, m)
    (X, Y), = re.findall(prize_reg, m)
    xa, ya, xb, yb, X, Y = int(xa), int(ya), int(xb), int(yb), int(X), int(Y)

    total_cost1 += calculate_cost(xa, xb, ya, yb, X, Y, False)
    total_cost2 += calculate_cost(xa, xb, ya, yb, X, Y, True)

print("Part 1:", total_cost1)
print("Part 2:", total_cost2)

    
