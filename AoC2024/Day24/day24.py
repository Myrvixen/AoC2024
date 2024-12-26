from queue import SimpleQueue

with open("day24.txt") as f:
    gates_str, conns_str = f.read().split("\n\n")

    gates = {}
    for line in gates_str.splitlines():
        gate, state = line.split(": ")
        gates[gate] = int(state)
        
    conns = [tuple(line.split()) for line in conns_str.splitlines()]

ops = {"AND": lambda a, b: a & b, "OR": lambda a, b: a | b, "XOR": lambda a, b: a ^ b}
Q = SimpleQueue()
for c in conns:
    Q.put(c)
while not Q.empty():
    c = Q.get()
    in1, op, in2, _, out = c
    if in1 not in gates or in2 not in gates:
        Q.put(c)
    else:
        gates[out] = ops[op](gates[in1], gates[in2])

z_vals = sorted([k for k in gates if k[0] == "z"])
val = int("".join([str(gates[z]) for z in z_vals[::-1]]), 2)

print("Part 1:", val)