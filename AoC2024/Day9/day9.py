with open("test.txt") as f:
    memory = f.read().strip()

files = memory[::2]
space = memory[1::2]
IDs = list(range(len(files)))

print(files)
print(space)
print(IDs)
