from collections import deque

def bfs(board, start):
    q = deque()
    q.append(start)
    board[start[0]][start[1]] = 0   # 방문 표시
    cnt = 1

    moves = [(1,0),(-1,0),(0,1),(0,-1)]  # 방향(상하좌우)

    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt


if __name__ == "__main__":
    N = int(input())
    board = []
    for _ in range(N):
        row = list(map(int, input().strip()))
        board.append(row)

    ans = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ans.append(bfs(board, (i,j)))

    print(len(ans))
    for x in sorted(ans):
        print(x)