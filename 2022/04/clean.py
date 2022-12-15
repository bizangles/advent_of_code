total = 0
total2 = 0
with open('input') as fh:
    for line in fh:
        pair = [list(map(int, p.split('-'))) for p in line.strip().split(',')]
        print(pair)
        pair = [set(range(p[0], p[1]+1)) for p in pair]
        overlap = pair[0] & pair[1]
        if overlap == pair[0] or overlap == pair[1]:
            total += 1
        if overlap:
            total2 += 1
print(total)
print(total2)

