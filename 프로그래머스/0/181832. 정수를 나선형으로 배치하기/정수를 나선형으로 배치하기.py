# 260323

def solution(n):
    answer = [[]]
    
    # 값을 0으로 채운 2차원 배열 생성
    answer = [ [0]*n for _ in range(n) ]
    
    # 위치변수
    x, y = 0, 0
    dx = [0, 1, 0, -1] # 행 이동 (세로)
    dy = [1, 0, -1, 0] # 열 이동 (가로)
    direction = 0 ### 0:오른쪽 / 1:아래쪽 / 2:왼쪽 / 3:위쪽 이동
    
    # 숫자 채우며 이동
    for num in range(1, n**2+1):
        answer[x][y] = num
        nx = x+dx[direction]
        ny = y+dy[direction]
        if nx<0 or nx>=n or ny<0 or ny>=n or answer[nx][ny]!=0:
            direction = (direction+1)%4
            nx = x+dx[direction]
            ny = y+dy[direction]
        x = nx
        y = ny
    
    
    return answer