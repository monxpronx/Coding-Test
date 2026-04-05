# 260405

n = int(input())

for i in range(1, n+1):
    tmp = " " * (n-i)
    for j in range(i):
        tmp += "*"
    print(tmp)