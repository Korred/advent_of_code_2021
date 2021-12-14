from collections import Counter
from functools import lru_cache

with open("input.txt", "r") as instructions:
    insertion = {}
    for e, i in enumerate(instructions):
        if e == 0:
            template = tuple(i.strip())
            
        elif e > 1:
            l, r = i.strip().split(" -> ")
            
            insertion[tuple(l)] = r
            
pair_counter = Counter(zip(template, template[1:]))
steps = 10

for step in range(steps):
    new_pair_counter = Counter()
    
    for pair in pair_counter.keys():
        left, right = pair
        to_insert = insertion[pair]
        
        new_pair_counter[(left, to_insert)] += pair_counter[pair]
        new_pair_counter[(to_insert, right)] += pair_counter[pair]
    
    pair_counter = new_pair_counter

single_counter = Counter()
for pair, cnt in pair_counter.items():
    # only consider right element of each pair since the left element is also part of the next pair
    single_counter[pair[1]] += cnt

# add back the first left element since it is not repeated by any other pair
single_counter[template[0]] += 1

most_common, least_common = single_counter.most_common()[0][1], single_counter.most_common()[-1][1]

diff = most_common - least_common
print(diff)