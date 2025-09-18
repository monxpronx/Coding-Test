from collections import deque

def bfs(town, start):
    q = deque()
    q.append(start)
    town[start[0]][start[1]] = 0   # 방문 표시 (방문하면 1->0으로 바꿀것)
    cnt = 1

    moves = [(1,0),(-1,0),(0,1),(0,-1)]  # 방향(상하좌우)

    while q:
        curr_x, curr_y = q.popleft()

        for dx, dy in moves:
            next_x, next_y = curr_x+dx, curr_y+dy
            if next_x < 0 or next_y < 0 or next_x >= len(town) or next_y >= len(town):  # 지도 밖으로 나가버리는 경우
                continue
            if town[next_x][next_y] == 1:
                town[next_x][next_y] = 0  # 방문표시
                q.append((next_x,next_y))  # 집 추가요
                cnt += 1
    return cnt


if __name__ == "__main__":

    N = int(input())
    town = []
    for _ in range(N):
        row = list(map(int, input().strip()))
        town.append(row)

    ans = []
    for i in range(N):
        for j in range(N):
            if town[i][j] == 1:
                ans.append(bfs(town, (i,j)))  # 방문하지않은 집(1) 발견하면 BFS수행

    print(len(ans))
    for x in sorted(ans):
        print(x)