# 260524

def factorial(n):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
    return tmp

N = int(input())
print(factorial(N))