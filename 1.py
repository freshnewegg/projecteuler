answer = 0

base = 3
for x in range(3,1000,3):
    answer+=x

for x in range(5,1000,5):
    if x%3!=0:
        answer+=x

print(answer)
