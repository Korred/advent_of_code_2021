from collections import deque

# find valid neighbours (their x,y position)
def get_neighbours(grid, node):
    terms = [(-1, 1),(0, 1),(1,1),(-1, 0),(1, 0),(-1,-1),(0,-1), (1,-1)]
    x_size, y_size = len(grid[0]) - 1, len(grid) - 1

    x, y = node
    for (tx, ty) in terms:
        if 0 <= x + tx <= x_size and 0 <= y + ty <= y_size:
            yield (x + tx, y + ty)

energy_levels = [[int(o) for o in line.strip()] for line in open("input.txt", "r")]

i = 0
while True:  
    # increase step counter
    i+=1
    
    # increase all energy levels by 1 and find positions that will flash
    to_flash = deque()
    seen = set()
    for y, line in enumerate(energy_levels):
        for x, loc in enumerate(line):
            energy_levels[y][x] += 1
            if energy_levels[y][x] > 9:
                to_flash.append((x,y))
                seen.add((x,y))
        
    # flash octopus, update neighbours and add relevant octopus to to_flash
    while to_flash:
        x,y = to_flash.popleft()
        
        # reset to 0
        energy_levels[y][x] = 0
        
        # find neighbour positions
        neighbours = get_neighbours(energy_levels, (x,y))
        for (nx, ny) in neighbours:
            if energy_levels[ny][nx] != 0:
                energy_levels[ny][nx] += 1
                if energy_levels[ny][nx] > 9 and (nx,ny) not in seen:
                    to_flash.append((nx,ny))
                    seen.add((nx,ny))
        
    if len(seen) == 100:
        break
    
print(f"The first step during which all octopuses flash: {i}")