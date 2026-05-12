# 260512

T = int(input())

for i in range(1, T+1):

    num_list = list(map(int, input().split()))
    total = sum(num_list)
    print("#{} {:.0f}".format(i, total/10))