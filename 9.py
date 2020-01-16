a = 1
b = 2
c = 3

import math
def is_sq(n):
    a = int(math.sqrt(n))
    if a**a == n:
        return True

    return False

t = 1000

a=1
b=1
c=998

for x in range(1,t+1):
    for y in range(1,t+1):
        z = t-x-y
        if x**2+y**2==z**2:
            # print(x,y,z)
            print(x*y*z)
            break


