from sys import stdout

class CPU:
    def __init__(self):
        self.cycle = 0
        self.regx = 1
        self.power = 0

    def noop(self):
        self.cycle += 1
        if not ((self.cycle-20) % 40) and self.cycle <= 220:
            # print((self.cycle, self.regx))
            self.power += self.cycle * self.regx
        self.draw_pixel()

    def draw_pixel(self):
        pos = (self.cycle - 1) % 40
        if pos >= self.regx - 1 and pos <= self.regx + 1:
            self.write('#')
        else:
            self.write('.')

    def write(self, c):
        stdout.write(c)
        if not self.cycle % 40:
            stdout.write("\n")

    def regx_add(self, n):
        self.noop()
        self.regx += n

cpu = CPU()
with open('input') as fh:
    for line in fh:
        ins = line.split()
        cpu.noop()
        if ins[0] == 'addx':
            cpu.regx_add(int(ins[1]))

print(cpu.power)

