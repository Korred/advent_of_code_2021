import re

x1, x2, y1, y2 = map(
    int, re.findall("([-\d]+)", open("test_input.txt", "r").readline().strip())
)

# n-th triangular number - Gauss
def triangular_num(n):
    return (n ** 2 + n) // 2


# regardless of the y-velocity (vy) chosen, after going up, the probe will eventually come back to x=?, y=0 (disregard x here)
# after reaching y=0, the current y-velocity will be the negative starting vy eg. at start: vy=9 - vy after coming back to y=0: vy=-9
# the next y position will be vy -= 1: eg. after reaching y=0 the next y will be y=-10 (due to gravity)
# to maximize the y-velocity vy, after reaching y=0, the next y position should be the lowest point in the targetbox
# eg. targetbox min(y) = -4 then vy should be 3
# trajectory only on y: (?,0) ->+3 (?,3) ->+2 (?,5) ->+1 (?,6) ->+0 (?,6) ->-1 (?,5) ->-2 (?,3) ->-3 (?,0) ->-4 (?,-4)
# max y position is the vy-th triangular number

vy = abs(y1) - 1
max_y_pos = triangular_num(vy)

print(max_y_pos)
