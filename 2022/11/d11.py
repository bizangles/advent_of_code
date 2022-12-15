class Monkey:
    def __init__(self, lines):
        self.holding = list(map(int, lines[0].split(': ')[1].split(', ')))
        self.operation_str = lines[1][19:].strip()
        self.operate = lambda old: eval(self.operation_str)
        self.test_num = int(lines[2][21:])
        self.true_monkey = int(lines[3][29:])
        self.false_monkey = int(lines[4][30:])
        self.inspect_count = 0
        self.max_val = None

    def inspect_all(self, monkeys):
        while self.holding:
            self.inspect_count += 1
            item = self.holding.pop()
            val = self.operate(item) % self.max_val
            toss_to = self.true_monkey if not val % self.test_num else self.false_monkey
            monkeys[toss_to].holding.append(val)

    def __repr__(self):
        return (
            f"Monkey:\n"
            f"  holding={self.holding}\n"
            f"  operation={self.operation_str}\n"
            f"  test_num={self.test_num}\n"
            f"    true={self.true_monkey}\n"
            f"    false={self.false_monkey}\n"
        )


with open('input') as fh:
    inp = fh.readlines()


monkeys = [
    Monkey(inp[n*7+1:n*7+6])
    for n in range(8)
]

from functools import reduce
max_val = reduce((lambda x, y: x*y), (m.test_num for m in monkeys))
for monkey in monkeys:
    monkey.max_val = max_val

for rn in range(10000):
    for monkey in monkeys:
        monkey.inspect_all(monkeys)


inspections = sorted((m.inspect_count for m in monkeys), reverse=True)
print(inspections)
print(inspections[0] * inspections[1])
