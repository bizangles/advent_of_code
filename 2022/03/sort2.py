pri = lambda c: (ord(c) - 97) % 58 + 1

total = 0
with open('input') as fh:
    group = []
    for line in fh:
        items = list(line.strip())
        group.append(set(items))
        if len(group) == 3:
            common = group[0] & group[1] & group[2]
            total += pri(common.pop())
            group = []

print(total)

