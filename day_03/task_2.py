report = [line.strip() for line in open("input.txt", "r")]


def get_rating(report, rating_type):
    grouped_bits = zip(*report)

    if rating_type == "gamma":
        return int("".join([max(set(g), key=g.count) for g in grouped_bits]), 2)

    if rating_type == "epsilon":
        return int("".join([min(set(g), key=g.count) for g in grouped_bits]), 2)

    if rating_type in ["oxygen", "co2"]:
        to_skip = set()

        for group in grouped_bits:
            # break prematurely if only one number is left
            if len(to_skip) == len(report) - 1:
                break

            counted = [0, 0]
            idx_lkp = {"0": [], "1": []}

            for e, bit in enumerate(group):
                if e not in to_skip:
                    counted[int(bit)] += 1
                    idx_lkp[bit].append(e)

            if rating_type == "oxygen":
                to_skip.update(idx_lkp["0"]) if counted[1] >= counted[0] else to_skip.update(idx_lkp["1"])

            elif rating_type == "co2":
                to_skip.update(idx_lkp["1"]) if counted[0] <= counted[1] else to_skip.update(idx_lkp["0"])

        return int(report[list(set(range(len(report))) - to_skip)[0]], 2)

    else:
        return "Unknown rating type provided"


oxygen_gen_rating = get_rating(report, "oxygen")
co2_scrub_rating = get_rating(report, "co2")

print(
    f"Oxygen generator rating ({bin(oxygen_gen_rating)}) {oxygen_gen_rating} *  CO2 scrubber rating ({bin(co2_scrub_rating)}) {co2_scrub_rating} = {oxygen_gen_rating * co2_scrub_rating}"
)

