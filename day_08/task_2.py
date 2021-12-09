from itertools import permutations

# index denotes the displayed number eg. "abcefg" == 0, "cf" == 1 etc...
digits_lkp = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

# calculate all possible segement permutations that will be used to translate digits_lkp
segments_permutations = permutations("abcdefg", 7)

# create a lookup that will take a set of segments and will return a translated digits_lkp
segments_lkp = {}
for perm in segments_permutations:
    trans_table = str.maketrans("abcdefg", "".join(perm))
    # translate and sort chars to get ascending alphab. order
    translated = ["".join(sorted(digit.translate(trans_table))) for digit in digits_lkp]

    # set is mutable - use immutable frozenset instead
    key = frozenset(translated)

    segments_lkp[key] = translated


with open("input.txt", "r") as data:
    line_sum = 0
    for e, line in enumerate(data):
        patterns, output = line.split(" | ")

        # ensure patterns are also sorted in alphab. order to match key in segments_lkp
        patterns = frozenset(["".join(sorted(pattern)) for pattern in patterns.strip().split(" ")])
        output = ["".join(sorted(digit)) for digit in output.strip().split(" ")]
        # get correct segments_lkp entry and decode string to number
        decoded_output = int("".join([str(segments_lkp[patterns].index(digit)) for digit in output]))
        line_sum += decoded_output

    print(line_sum)
