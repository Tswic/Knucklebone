from debug_rapid import *


l = [0, 0]
for i in range(300):
    t = robot_printless(3)
    if t >= 0:
        l[0] += 1
    if t <= 0:
        l[1] += 1
    print(i, "/", 300)
print(l)
