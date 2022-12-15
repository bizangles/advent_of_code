import curses
import sys
import time


with open('input') as fh:
    m = list(l.strip() for l in fh.readlines())

wid = len(m[0])
hig = len(m)
start = None
end = None

sys.setrecursionlimit(wid*hig)

for y in range(hig):
    sx = None
    try:
        sx = m[y].index('S')
    except ValueError:
        pass
    else:
        start = (sx, y)

    try:
        ex = m[y].index('E')
    except ValueError:
        continue
    else:
        end = (ex, y)

    if start and end:
        break

hmap = {(x,y): ord(m[y][x])-97 for x in range(wid) for y in range(hig)}
hmap[start] = ord('a')-97
hmap[end] = ord('z')-97


all_start = {s for s, h in hmap.items() if h == 0}


def valid_step(s):
    return s[0]>=0 and s[0]<wid and s[1]>=0 and s[1]<hig


def find_path(frm, to, window=None):
    visited = set()
    count = 0
    path_to = {f: set([f]) for f in frm}

    steps = frm
    while True:
        next_steps = set()
        visited |= steps

        if not steps:
            return None

        valid_path = set()
        invalid_path = set()

        for step in steps:
            if m[step[1]][step[0]] == 'E':
                if window:
                    for s in visited-path_to[step]:
                        window.addch(s[1], s[0], m[s[1]][s[0]], curses.color_pair(2))
                    for s in path_to[step]:
                        window.addch(s[1], s[0], m[s[1]][s[0]], curses.color_pair(3))
                    window.refresh()
                    time.sleep(5)
                return count

            has_steps = {
                s for s in (
                    (step[0]-1, step[1]),
                    (step[0]+1, step[1]),
                    (step[0], step[1]-1),
                    (step[0], step[1]+1),
                ) if (
                    valid_step(s) and
                    s not in visited and
                    hmap[s] <= hmap[step] + 1
                )
            } - next_steps

            if not has_steps:
                invalid_path |= path_to[step]
            else:
                valid_path |= path_to[step]
                for ns in has_steps:
                    path_to[ns] = path_to[step] | {ns}
                    next_steps.add(ns)

        invalid_path -= valid_path

        if window:
            for step in invalid_path:
                window.addch(step[1], step[0], m[step[1]][step[0]], curses.color_pair(2))
            for step in valid_path:
                window.addch(step[1], step[0], m[step[1]][step[0]], curses.color_pair(4))

            window.refresh()
            time.sleep(0.02)

        steps = next_steps
        count += 1


def init(window):
    window.clear()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

def animate(window):
    init(window)
    for n, row in enumerate(m):
        window.addstr(row + "\n", curses.color_pair(0))
    fin = find_path({start}, end, window=window)
    return fin

def animate2(window):
    init(window)
    for n, row in enumerate(m):
        window.addstr(row + "\n", curses.color_pair(0))
    fin = find_path(all_start, end, window=window)
    return fin

ans1 = curses.wrapper(animate)
ans2 = curses.wrapper(animate2)

print(ans1)
print(ans2)


