from itertools import product
from functools import cache

rows = open("input.txt", "r").read().split("\n")
p1_pos, p2_pos = (map(int, [row.split(" ")[-1] for row in rows]))
outcomes = tuple(product((1, 2, 3), repeat=3))


@cache
def play(p1_pos, p2_pos, p1_score, p2_score):
    wins = [0, 0]

    for outcome in outcomes:
        to_move = sum(outcome)
        px_pos = (p1_pos + to_move) % 10 or 10
        px_score = p1_score + px_pos
        
        if px_score >= 21:
            wins[0] += 1
        else:
            wins2, wins1 = play(p2_pos, px_pos, p2_score, px_score)
            wins[0] += wins1
            wins[1] += wins2
    
    return wins


wins = play(p1_pos, p2_pos, 0, 0)
print(max(wins))