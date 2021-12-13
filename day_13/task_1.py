with open("input.txt", "r") as information:
    dots = []
    instructions = []
    x_max, y_max = 0, 0

    for line in information:
        if line[0].isnumeric():
            x,y = list(map(int, line.strip().split(",")))
            dots.append((x,y))
            x_max = max(x_max, x)
            y_max = max(y_max, y)
        
        elif line[0] == "f":
            axis, num = line.strip().split(" ")[2].split("=")
            instructions.append((axis, int(num)))


    paper = [[" "]*(x_max+1) for y in range(y_max+1)]
    for (x,y) in dots:
        paper[y][x] = "#"
   
    
for (axis, idx) in instructions:
    if axis == "y":
        for l_idx in range(idx+1, len(paper)):
            for x, pos in enumerate(paper[l_idx]):
                if pos == "#":
                    paper[(2*idx)- l_idx][x] = "#"
                    
        del paper[idx:]
        
        
    if axis == "x":
        for y, line in enumerate(paper):
            
            for c_idx in range(idx+1, len(line)):
                for pos in line[c_idx]:
                    if pos == "#":
                        paper[y][(2*idx) - c_idx] = "#"
                                    
            del paper[y][idx:]
            
    break
    

dots_cnt = 0    
for line in paper:
    dots_cnt += line.count("#")
    
print(dots_cnt)