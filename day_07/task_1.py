crabs = sorted(map(int, open("input.txt", "r").readline().strip().split(",")))

# position with minimal fuel usage is at the median position
median_pos = crabs[len(crabs) // 2]
min_fuel = sum([abs(crab_pos - median_pos) for crab_pos in crabs])

print(min_fuel)
