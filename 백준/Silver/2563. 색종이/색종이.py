# 260413

board = [[0]*100 for _ in range(100)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            board[x+j][y+k] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j]==1:
            cnt+=1
print(cnt)