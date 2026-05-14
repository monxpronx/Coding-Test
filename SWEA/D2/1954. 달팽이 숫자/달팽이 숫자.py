# 260514

T = int(input())

for i in range(1, T+1):

    n = int(input())
    
    # nxn의 0행렬 생성
    matrix = []
    for j in range(n):
        matrix.append([0]*n)
    
    # 초기값 설정
    x, y = 0, 0
    d = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    num = 1

    # 시뮬레이션
    while num <= n*n:

        matrix[x][y] = num

        num+=1
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or n <= nx or ny < 0 or n <= ny or matrix[nx][ny]!=0:
            d = (d+1)%4
            nx = x + dx[d]
            ny = y + dy[d]
        x, y = nx, ny

    print("#{}".format(i))
    for j in range(n):
        print(*matrix[j])