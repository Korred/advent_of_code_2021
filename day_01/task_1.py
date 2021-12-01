depths = [int(line.strip()) for line in open("input.txt", "r")]

inc_counter = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        inc_counter += 1

print(f"{inc_counter} measurements are larger than the previous measurement!")
