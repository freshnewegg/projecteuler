'''

1 = 2 = 4 = 8
3 = 6
3 == 9
5 == 10
7

2520/10 = 252
2520/9 = 280

/10 (1,2,5,10)
/9 (3,9)
/8 (1,2,4,8)
/7 (7)
/6 (1,2,3,6)

20 (1,2,4,5,10,20)


'''


def all_good(k):
    for x in range(2,21):
        # print(k%x)
        if k%x!=0:
            return False

    return True

# print(all_good(2520))

for k in range(20, 1000000000, 20):
    # print(k)
    good = all_good(k)
    # print(good)≥
    if good:
        print(k)
        break


