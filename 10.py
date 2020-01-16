import math
def is_prime(x):
    if x%2==0:
        return False
    for i in range(3, math.floor(math.sqrt(x))+1,2):
        if x%i==0:
            return False
    return True

answer = 2
for x in range(3,2000000,2):
    if is_prime(x):
        answer+=x

print(answer)