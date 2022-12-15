score1 = {'X': 1, 'Y': 2, 'Z': 3}
score2 = {"AX": 3, "AY": 6, "AZ": 0, "BX": 0, "BY": 3, "BZ": 6, "CX": 6, "CY": 0, "CZ": 3}
choose = {"AX": "Z", "AY": "X", "AZ": "Y", "BX": "X", "BY": "Y", "BZ": "Z", "CX": "Y", "CY": "Z", "CZ": "X"}

total = 0
total2 = 0
with open('input') as fh:
    for line in fh:
        (opp, me) = line.split()
        total += score1[me] + score2[''.join((opp, me))]
        me2 = choose[''.join((opp, me))]
        total2 += score1[me2] + score2[''.join((opp, me2))]

print(total)


