import curses
import time

lines = []
with open('input') as fh:
    for line in fh:
        points = tuple(tuple(map(int, p.split(','))) for p in line.split(' -> '))
        for x in range(len(points)-1):
            lines.append((points[x], points[x+1]))


def myrange(a, b):
    return range(min(a, b), max(a, b)+1)


minx = 500
maxx = 500
maxy = 0

walls = set()
for line in lines:
    for x in myrange(line[0][0], line[1][0]):
        minx = min(minx, x)
        maxx = max(maxx, x)
        for y in myrange(line[0][1], line[1][1]):
            maxy = max(maxy, y)
            walls.add((x, y))

width = maxx - minx + 1
height = maxy + 1

for x in myrange(500 - height - 1, 500 + height + 1):
    walls.add((x, height + 1))

maxy += 2
height += 2


poo = {}
def draw_chr(pad, coord, c):
    pad_hig, pad_wid = pad.getmaxyx()
    left = 500 - int(pad_wid/2)
    try:
        pad.addch(coord[1], coord[0] - left, c)
    except:
        poo['err'] = coord
        raise


def draw_walls(pad):
    for w in walls:
        draw_chr(pad, w, '#')


def show_pad(pad, display, max_move):
    hig, wid = display
    pad_hig, pad_wid = pad.getmaxyx()

    mid_top = int(hig/2)
    mid_bot = hig - mid_top

    if max_move < mid_top:
        pad.refresh(0, 0, 0, 0, hig - 1, wid - 1)
    elif max_move > (pad_hig - mid_bot - 1):
        pad.refresh(pad_hig - hig, 0, 0, 0, hig - 1, wid - 1)
    else:
        pad.refresh(max_move - mid_top, 0, 0, 0, hig - 1, wid - 1)


def drop_sand(win):
    frame = 0
    moving = None
    settled = set()

    display = win.getmaxyx()

    pad = curses.newpad(maxy+3, maxy * 2 + 2)
    draw_walls(pad)
    draw_chr(pad, (500, 0), '+')
    show_pad(pad, display, 0)
    pad.getch()

    sand = None
    while True:
        sand = (500, 0)

        if sand in settled:
            break

        do_settle = None

        while do_settle is None:
            slope = []

            # Go down
            while (sand[0], sand[1]+1) not in walls | settled:
                if sand[1] > maxy - 3:
                    pad.getch()
                    return len(settled)
                sand = (sand[0], sand[1] + 1)

            # Go left
            if (sand[0] - 1, sand[1] + 1) not in walls | settled:
                while (
                    (sand[0], sand[1] + 1) in walls | settled and
                    (sand[0] - 1, sand[1] + 1) not in walls | settled
                ):
                    if (sand[0] + 1, sand[1] + 1) not in walls | settled:
                        slope = []
                    sand = (sand[0] - 1, sand[1] + 1)
                    slope.append(sand)
            # Go right
            elif (sand[0] + 1, sand[1] + 1) not in walls | settled:
                while (
                    (sand[0], sand[1] + 1) in walls | settled and
                    (sand[0] - 1, sand[1] + 1) in walls | settled and
                    (sand[0] + 1, sand[1] + 1) not in walls | settled
                ):
                    sand = (sand[0] + 1, sand[1] + 1)
                    slope.append(sand)

            if (
                (sand[0], sand[1] + 1) in walls | settled and
                (sand[0] - 1, sand[1] + 1) in walls | settled and
                (sand[0] + 1, sand[1] + 1) in walls | settled
            ):
                do_settle = slope or [sand]

        if do_settle:
            for sand in do_settle:
                draw_chr(pad, sand, 'O')
                settled.add(sand)
            show_pad(pad, display, do_settle[0][1])
            sand = None

    pad.getch()
    return len(settled)


try:
    print(curses.wrapper(drop_sand))
except:
    print((minx, maxx))
    print(maxy)
    print(poo['err'])
