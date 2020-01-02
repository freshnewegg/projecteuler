import math
def is_prime(x):
    for i in range(3, math.floor(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

bignum = 600851475143
sr = math.floor(math.sqrt(bignum))
if sr%2==0:
    sr+=1
for x in range(sr,0, -2):
    if bignum%x==0:
        if is_prime(x):
            print(x)
            break