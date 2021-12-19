import re
from itertools import product

x1, x2, y1, y2 = map(
    int, re.findall("([-\d]+)", open("input.txt", "r").readline().strip())
)


def sim_trajectory(vx, vy):
    px, py = 0, 0

    while True:
        px += vx
        py += vy


        if px > x2 or py < y1:
            return 0

        if px >= x1 and py <= y2:
            return 1

        # adjust vx, vy
        # drag
        vx -= (vx>0)

        # gravity
        vy -= 1


hits = 0
for (x, y) in product(range(1, x2 + 1), range(y1, -y1)):
    hits += sim_trajectory(x,y)

print(hits)