from collections import deque

rows = open("input.txt", "r").read().split("\n")
players = deque([[int(row.split(" ")[-1]), 0] for row in rows]) # pos, score
rolls = 0
dice = deque(range(1,101))

while all([p[1] < 1000 for p in players]):
    to_move = sum([dice[i] for i in range(3)])
    dice.rotate(-3)
    rolls += 3
    
    players[0][0] = (players[0][0] + to_move) % 10 or 10
    players[0][1] += players[0][0]
    
    players.rotate(1)

res = min(players, key=lambda p: p[1])[1] * rolls
print(res)
