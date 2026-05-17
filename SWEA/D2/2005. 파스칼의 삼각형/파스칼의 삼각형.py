# 260517

T = int(input())

for t in range(1, T+1):

    N = int(input())
    pascal = []

    for i in range(N): # i는 0,1,2,3
        pascal.append([0] * (i+1))

        for j in range(i+1):
            if j==0 or j==i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print("#{}".format(t))
    for n in range(N):
        print(*pascal[n])