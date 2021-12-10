from collections import deque

lines = [line.strip() for line in open("input.txt", "r")]
valid_pairs = set([('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')])
points = {'(': 1, '[': 2, '{': 3, '<': 4}


completion_scores = []
for line in lines:
    queue = deque()
    corrupted = False
    
    # build up queue and skip corrupted lines
    for c in line:
        if c in ['(', '[', '{', '<']:
            queue.append(c)
        else:
            pair = (queue.pop(),c)
            if pair not in valid_pairs:
                corrupted = True
                break

    # fix only incomplete lines
    if not corrupted:
        total_score = 0
        while queue:
            total_score = (total_score*5) + points[queue.pop()]
            
        completion_scores.append(total_score)
            
            
completion_scores.sort()        
print(completion_scores[len(completion_scores)//2])