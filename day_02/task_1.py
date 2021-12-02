instructions = [line.strip().split(" ") for line in open("input.txt", "r")]

h_pos = 0
depth = 0

for i in instructions:
    num = int(i[1])

    # Structural Pattern Matching only in Python 3.10 - https://www.python.org/dev/peps/pep-0622/
    match i[0]:
        case "forward":
            h_pos += num
        case 'down':
            depth += num
        case 'up':
            depth -= num

print(f"Final horizonal position: {h_pos} - Final depth: {depth} - Multiplied: {h_pos * depth}")
