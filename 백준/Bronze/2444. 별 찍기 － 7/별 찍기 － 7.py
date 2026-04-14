# 260414

n = int(input())

for i in range(1, n+1):
    blank = " " * (n-i)
    star = "*" * (2*i-1)
    print(blank + star)

for j in range(n-1, 0, -1):
    blank = " " * (n-j)
    star = "*" * (2*j-1)
    print(blank + star)