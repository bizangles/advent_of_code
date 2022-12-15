from collections import defaultdict

with open('input') as fh:
    grid = [line.strip() for line in fh]
    

visible = set()
rows = len(grid)
cols = len(grid[0])

trees = defaultdict(list)

for row in range(rows):
    last_seen = defaultdict(lambda:0)
    for col in range(cols):
        n = int(grid[row][col])
        trees[(row, col)].append(col - last_seen[n])
        for x in range(n+1):
            last_seen[x] = col

    last_seen = defaultdict(lambda:cols-1)
    for col in reversed(range(cols)):
        n = int(grid[row][col])
        trees[(row, col)].append(last_seen[n] - col)
        for x in range(n+1):
            last_seen[x] = col

for col in range(cols):
    last_seen = defaultdict(lambda:0)
    for row in range(rows):
        n = int(grid[row][col])
        trees[(row, col)].append(row - last_seen[n])
        for x in range(n+1):
            last_seen[x] = row

    last_seen = defaultdict(lambda:rows-1)
    for row in reversed(range(rows)):
        n = int(grid[row][col])
        trees[(row, col)].append(last_seen[n] - row)
        for x in range(n+1):
            last_seen[x] = row

maxvis = 0
for k, v in trees.items():
    t = v[0] * v[1] * v[2] * v[3]
    if t > maxvis:
        maxvis = t
print(maxvis)
