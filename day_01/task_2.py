depths = [int(line.strip()) for line in open("input.txt", "r")]

inc_counter = 0

# (len(depths) - 2) windows of length 3 can fit into depths
for i in range(len(depths) - 2):
    a = sum(depths[i : i + 3])
    b = sum(depths[i + 1 : i + 4])

    if b > a:
        inc_counter += 1

print(f"{inc_counter} sums are larger than the previous sum!")
