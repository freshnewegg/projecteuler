def is_palindrome(n):
    s = str(n)
    for x in range(len(s) // 2):
        if s[x] != s[-(x + 1)]:
            return False
        ''' abc abcd'''
    return True

def lp(n):
    a = int("9" * n)
    b = int("9" * n)

    bound = int("9" * (n-1))
    answer = 0
    for i in range(a,bound,-1):
        for j in range(b,i,-1):
            if i*j<answer:
                continue
            if is_palindrome(i*j):
                answer = max(answer, i*j)
    return answer

import time
start = time.time()
print(lp(3))
end = time.time()
print(end-start)
