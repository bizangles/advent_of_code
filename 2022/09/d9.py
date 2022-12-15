steps = []
with open('input') as fh:
    for line in fh:
        d, n = line.split()
        steps += [d] * int(n)

def do_move(k1, k2):
    if abs(k1[1] - k2[1]) == 2 or abs(k1[0] - k2[0]) == 2:
        return (k1[0] + int((k2[0] - k1[0])/2), k1[1] + int((k2[1] - k1[1])/2))
    return k2

minpos = [0,0]
k = [(0,0) for x in range(10)]

all_pos = [set() for x in range(10)]

# tpos = []

for step in steps:
    if step == 'U':
        k[0] = (k[0][0], k[0][1]+1)
    elif step == 'D':
        k[0] = (k[0][0], k[0][1]-1)
    elif step == 'R':
        k[0] = (k[0][0]+1, k[0][1])
    elif step == 'L':
        k[0] = (k[0][0]-1, k[0][1])

    for x in range(9):
        k[x+1] = do_move(k[x], k[x+1])

    for x in range(10):
        all_pos[x].add(k[x])
        minpos[0] = min(minpos[0], k[x][0])
        minpos[1] = min(minpos[1], k[x][1])

    # tpos.append(k[-1])

print(list(len(a) for a in all_pos))

# def print_tpos(window):
#     minx = min(t[0] for t in tpos)
#     miny = min(t[1] for t in tpos)
#     for x,y in tpos:
#         window.addch(y-miny,x-minx,'#')
#     window.getch()
# 
# import curses
# curses.wrapper(print_tpos)
