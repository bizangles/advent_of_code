pri = lambda c: (ord(c) - 97) % 58 + 1

total = 0
with open('input') as fh:
    for line in fh:
        items = list(line.strip())
        half = int(len(items)/2)
        sack1 = items[:half]
        sack2 = items[half:]
        common = set(sack1) & set(sack2)
        total += pri(common.pop())

print(total)

