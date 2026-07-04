# 260704

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split())) # 길이 N
    B = list(map(int, input().split())) # 길이 M

    if len(A) > len(B):
        long_arr, short_arr = A, B
    else:
        long_arr, short_arr = B, A

    max_value = 0
    for i in range(len(long_arr)-len(short_arr)+1): # 각 시작점 i
        value = 0
        for j in range(len(short_arr)):
            value += (short_arr[j] * long_arr[i+j]) 
        if max_value < value:
            max_value = value

    print("#{} {}".format(t, max_value))