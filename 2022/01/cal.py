import bisect


def main():
    elves = []
    top3 = []
    with open('input') as fh:
        elf = []
        for line in fh:
            line = line.strip()
            if not line:
                add_elf(elves, elf)
                elf = []
                continue
            cals = int(line)
            elf.append(cals)
        if elf:
            add_elf(elves, elf)
    
    print(sum(e[0] for e in elves[-3:]))


def add_elf(elves, elf):
    n = len(elves)
    total = sum(elf)
    bisect.insort(elves, (total, n, elf))


if __name__ == "__main__":
    main()

