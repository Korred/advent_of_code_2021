crabs = list(map(int, open("input.txt", "r").readline().strip().split(",")))

# n-th triangular number - Gauss
def terminal(n):
    return (n ** 2 + n) // 2


min_fuel = None
for pos in range(min(crabs), max(crabs) + 1):
    fuel_sum = sum([terminal(abs(crab_pos - pos)) for crab_pos in crabs])

    if not min_fuel:
        min_fuel = fuel_sum
    else:
        min_fuel = fuel_sum if fuel_sum < min_fuel else min_fuel

print(min_fuel)
