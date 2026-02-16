# 260216

def solution(board):
    
    side = len(board)
    answer = side*side
    
    for i in range(side):
        for j in range(side):
            flag = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (0<=i+dx<side) and (0<=j+dy<side) and (board[i+dx][j+dy]==1):
                        answer-=1
                        flag = 1
                        break
                if flag == 1:
                    break
    
    return answer