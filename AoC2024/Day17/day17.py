with open("day17.txt") as f:
    regs, program = f.read().split("\n\n")
    A, B, C = [int(line.split()[2]) for line in regs.splitlines()]
    program = [int(ops) for ops in program.split()[1].split(",")]
    #registers = {"A": A, "B": B, "C": C}

def get_combo_operand(x):
    if 0 <= x <= 3:
        return x
    elif 4 <= x <= 6: 
        return {4: A, 5: B, 6:C}[x]

p = 0
output = ""
while p < len(program):
    opcode, operand = program[p], program[p+1]
    if opcode == 0:  # adv
        operand = get_combo_operand(operand)
        A = A // 2**operand
    elif opcode == 1:   # bxl
        B = B ^ operand
    elif opcode == 2:  # bst
        operand = get_combo_operand(operand)
        B = operand % 8
    elif opcode == 3:  # jnz
        if A != 0:
            p = operand
            continue
    elif opcode == 4:  # bxc
        B = B ^ C
    elif opcode == 5:  # out
        operand = get_combo_operand(operand)
        output += f"{operand % 8},"
    elif opcode == 6:  # bdv
        operand = get_combo_operand(operand)
        B = A // 2**operand
    elif opcode == 7:
        operand = get_combo_operand(operand)
        C = A // 2**operand
    p += 2

output = output[:-1]

print("Part 1:", output)
