with open("day23.txt") as f:
    lines = f.read().splitlines()

conns = {}
for conn in lines:
    a, b = conn.split("-")
    if a in conns:
        conns[a].add(b)
    else:
        conns[a] = set([b])
    if b in conns:
        conns[b].add(a)
    else:
        conns[b] = set([a])

num_sets = 0
longest_set = set()
for c in conns:
    if not c[0] == "t":
        continue

    set_counts = {}
    for o in conns[c]:

        sets = conns[c].intersection(conns[o])

        if o[0] != "t":  # avoid triple counting
            num_sets += len(sets)
            
        sets.update([c, o])
        #sets.add(o)
        if tuple(sets) in set_counts:
            set_counts[tuple(sets)] += 1
        else:
            set_counts[tuple(sets)] = 1
    
    for s, count in set_counts.items():
        #if len(s) == count and (len(s) + 1) > len(longest_set):
        if len(s) == count + 1 and len(s) > len(longest_set):
            longest_set = set(s)
            #longest_set.add(c)
        

password = ",".join(sorted(list(longest_set)))

print("Part 1:", num_sets / 2)
print("Part 2:", password)