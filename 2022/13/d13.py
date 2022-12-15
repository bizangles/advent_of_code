from functools import cmp_to_key

all_items = [[[2]], [[6]]]
pairs = []
with open('input') as fh:
    pair = []
    for line in fh:
        line = line.strip()
        if not line:
            pairs.append(pair)
            pair = []
            continue

        item = eval(line)
        pair.append(item)
        all_items.append(item)
    pairs.append(pair)


def compare(left, right):
    ltype = type(left) == int
    rtype = type(right) == int

    if ltype and not rtype:
        return compare([left], right)
    if rtype and not ltype:
        return compare(left, [right])

    try:
        if left < right:
            return -1
        if left > right:
            return 1
        return 0
    except TypeError:
        for i in range(min(len(left), len(right))):
            c = compare(left[i], right[i])
            if not c:
                continue
            return c
        return c

    return compare(len(left), len(right))

#sorted_pairs = sorted(pairs, 
print(sum(c for c in (compare(*pair) for pair in pairs) if c < 0))

all_sorted = sorted(all_items, key=cmp_to_key(compare))
for a in all_sorted:
    print(a)
print((all_sorted.index(all_items[0])+1) * (all_sorted.index(all_items[1])+1))

