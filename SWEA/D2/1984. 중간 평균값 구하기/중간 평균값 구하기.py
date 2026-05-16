# 260516

T = int(input())

for t in range(1, T+1):

    num_list = list(map(int, input().split()))
    num_list.sort()
    num_list = num_list[1:9]
    avg = sum(num_list) / 8.0
    print("#{} {:.0f}".format(t, avg))