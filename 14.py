def next(n):
    if n%2==0:
        a=n/2
    else:
        a=3*n+1
    return a

numans = 0
ans = 0


mem = {}

for x in range(1,1000001):
    n = x
    total = 1
    while(n!=1):
        n=next(n)

        if n in mem:
            total+=mem[n]
            n=1
        else:
            total+=1

    mem[x]=total

    if total > ans:
        ans = total
        numans = x

# print(mem)
print(ans, numans)
