n = 100

s = 0
ss = 0
for x in range(1,100+1):
    s+=x**2
    ss+=x

print(ss)
print(s)
print(ss**2-s)