import math
def is_prime(x):
    for i in range(3, math.floor(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

c = 1
h = 0
for x in range(3, 1000000, 2):
    if is_prime(x):
        c+=1
        h=x
        if c == 10001:
            break

print(c,h)