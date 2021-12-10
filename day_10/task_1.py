from collections import deque

lines = [line.strip() for line in open("input.txt", "r")]
valid_pairs = set([('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')])
points = {')': 3, ']': 57, '}': 1197, '>': 25137}


syntax_error_score = 0
for line in lines:
    queue = deque()
    
    for c in line:
        if c in ['(', '[', '{', '<']:
            queue.append(c)
        else:
            pair = (queue.pop(),c)
            if pair not in valid_pairs:
                syntax_error_score += points[c]
                break

print(syntax_error_score)