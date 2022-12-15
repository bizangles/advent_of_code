sensors = [
    ((2793338, 1910659),(2504930, 2301197)),
    ((2887961, 129550),(2745008, -872454)),
    ((3887055, 2785942),(4322327, 2605441)),
    ((3957399, 2164042),(3651713, 1889668)),
    ((1268095, 1265989),(1144814, 2000000)),
    ((2093967, 2103436),(2504930, 2301197)),
    ((2980126, 1348046),(3651713, 1889668)),
    ((508134, 3998686),(1123963, 4608563)),
    ((2982740, 3604350),(2756683, 3240616)),
    ((2372671, 3929034),(2756683, 3240616)),
    ((437628, 1124644),(570063, 959065)),
    ((3271179, 3268845),(3444757, 3373782)),
    ((1899932, 730465),(570063, 959065)),
    ((1390358, 3881569),(1123963, 4608563)),
    ((554365, 989190),(570063, 959065)),
    ((2225893, 2703661),(2504930, 2301197)),
    ((3755905, 1346206),(3651713, 1889668)),
    ((3967103, 3930797),(3444757, 3373782)),
    ((3534099, 2371166),(3651713, 1889668)),
    ((3420789, 1720583),(3651713, 1889668)),
    ((2222479, 3278186),(2756683, 3240616)),
    ((100457, 871319),(570063, 959065)),
    ((1330699, 2091946),(1144814, 2000000)),
    ((598586, 99571),(570063, 959065)),
    ((3436099, 3392932),(3444757, 3373782)),
    ((3338431, 3346334),(3444757, 3373782)),
    ((3892283, 688090),(3651713, 1889668)),
    ((1485577, 1929020),(1144814, 2000000)),
    ((2991003, 2951060),(2756683, 3240616)),
    ((2855486, 2533468),(2504930, 2301197)),
    ((750865, 1619637),(1144814, 2000000)),
    ((3378101, 3402212),(3444757, 3373782)),
    ((3515528, 2950404),(3444757, 3373782)),
    ((163133, 2640553),(-1016402, 3057364)),
    ((1765550, 3021994),(2756683, 3240616)),
    ((534625, 1056421),(570063, 959065)),
    ((3418549, 3380980),(3444757, 3373782)),
    ((29, 389033),(570063, 959065)),
]

row = 2000000

nobeacon = set()

for sensor, beacon in sensors:
    dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    amp = dist - abs(sensor[1] - row)
    if amp > 0:
        nobeacon |= set(range(sensor[0]-amp, sensor[0]+amp))

print(len(nobeacon))


def calc(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


in_range = lambda b: b[0] >= 0 and b[0] <= 4000000 and b[1] >= 0 and b[1] <= 4000000

borders = set()
for sensor, beacon in sensors:
    print(f"Adding: {sensor}")
    dist = calc(sensor, beacon) + 1
    for n in range(dist * 2 + 1):
        b1 = (sensor[0] - dist + n, sensor[1] + n)
        if in_range(b1):
            borders.add(b1)
        b2 = (sensor[0] - dist + n, sensor[1] - n)
        if in_range(b2):
            borders.add(b2)


print(len(borders))


for sensor, beacon in sensors:
    print(f"Removing: {sensor} - {len(borders)}")
    dist = calc(sensor, beacon)
    keep = set()
    borders = set(filter(lambda b: calc(sensor, b) > dist, borders))

print(borders)
