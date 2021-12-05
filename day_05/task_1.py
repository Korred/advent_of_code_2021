from collections import defaultdict

with open("input.txt", "r") as lines:
    vents = defaultdict(int)

    for line in lines:
        # get lines and order them to always go from left to right
        (x1, y1), (x2, y2) = sorted(map(lambda x: list(map(int, x.split(","))), line.strip().split(" -> ")), key=lambda e: e[0])

        # vertical line
        if x1 == x2:
            # ensure that line is rising
            start, end = (y1, y2) if y1 < y2 else (y2, y1)
            for y in range(start, end + 1):
                vents[(x1, y)] += 1

        # horizontal line
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                vents[(x, y1)] += 1


dangerous_cnt = len(dict((k, v) for k, v in vents.items() if v >= 2))
print(f"Number of points where at least two lines overlap: {dangerous_cnt}")
