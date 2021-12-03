report = [line.strip() for line in open("input.txt", "r")]
grouped_bits = zip(*report)

gamma_rate = int("".join([max(set(g), key=g.count) for g in grouped_bits]), 2)
epsilon_rate = gamma_rate ^ (2 ** len(report[0]) - 1)  # xor with 11111... to inverse bits

print(
    f"Gamma rate ({bin(gamma_rate)}) {gamma_rate} *  Epsilon rate ({bin(epsilon_rate)}) {epsilon_rate} = {gamma_rate * epsilon_rate}"
)

