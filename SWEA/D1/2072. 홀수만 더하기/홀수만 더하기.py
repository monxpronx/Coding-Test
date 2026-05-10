# 260510

T = int(input())
for i in range(T):
    temp = list(map(int, input().split()))
    total = 0
    for j in range(10):
        if temp[j]%2==1:
            total+=temp[j]
    print("#{} {}".format(i+1, total))