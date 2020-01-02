a, b = 1, 1

answer = 0

while a+b<4000000:
    c = a+b
    if c%2==0:
        answer+=c

    a = b
    b = c

print(answer)