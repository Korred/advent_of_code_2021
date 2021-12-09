with open("input.txt", "r") as data:

    easy_digits_cnt = 0
    for line in data:
        patterns, output = line.split(" | ")

        patterns = ["".join(sorted(pattern)) for pattern in patterns.strip().split(" ")]
        output = ["".join(sorted(digit)) for digit in output.strip().split(" ")]

        for digit in output:
            if len(digit) in (2, 3, 4, 7):
                easy_digits_cnt += 1

    print(easy_digits_cnt)
