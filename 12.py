s = 0
n=20000

import math
for x in range(1, n+1):
    s+=x
    factors = 0
    i = 1
    while i*i<=s:
        if i*i==s:
            factors+=1
        elif s%i==0:
            factors+=2
        i+=1
    if factors > 500:
        print(s)
        break