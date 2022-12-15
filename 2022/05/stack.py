stacked = False
stacks = [[] for i in range(9)]

with open('input') as fh:
    for line in fh:
        if line == "\n":
            continue

        if not stacked:
            if line[1] == "1":
                stacked = True
                continue

            for n in range(9):
                i = n*4+1
                if line[i] != " ":
                    stacks[n].insert(0, line[i])
            continue

        words = line.split()
        num = int(words[1])
        frm = int(words[3]) - 1
        too = int(words[5]) - 1

        print(f"{num} {frm} {too}")
        for n in range(num):
            stacks[too].append(stacks[frm].pop())

print(''.join(s[-1] for s in stacks))
