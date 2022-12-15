with open('input') as fh:
    buff = fh.read().strip()

last = []
for n, c in enumerate(buff):
    if len(last) == 14:
        last.pop(0)
    last.append(c)
    if len(set(last)) == 14:
        print(n+1)
        break
