# 260519

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        big, small = B, A
    else:
        big, small = A, B

    max_value = 0
    for i in range(len(big)-len(small)+1):
        value = 0
        for j in range(len(small)):
            value += (small[j] * big[i+j])
        if max_value < value:
            max_value = value
    
    print("#{} {}".format(t, max_value))