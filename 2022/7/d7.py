from collections import defaultdict

sizes = defaultdict(int)
curr = ['']

with open('input') as fh:
    for line in fh:
        command = line.split()

        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '/':
                    curr = ['']
                elif command[2] == '..':
                    curr.pop()
                else:
                    curr.append(command[2])
            if command[1] == 'ls':
                pass
        elif command[0] == 'dir':
            pass
        else:
            size, filename = command
            for n in range(len(curr)):
                dirname = '/'.join(curr[:n+1])
                sizes[dirname] += int(size)

MAXSIZE = 100000
total = 0

for dirname in sorted(sizes.keys()):
    if sizes[dirname] < MAXSIZE:
        print(dirname)
        total += sizes[dirname]

print(total)

TOTALSPACE = 70000000
SPACENEEDED = 30000000

del_at_least = sizes[''] - (TOTALSPACE - SPACENEEDED)

for dirname, size in sorted(sizes.items(), key=lambda x: x[1]):
    if size >= del_at_least:
        print((dirname, size))
        break
