# 260213

def solution(keyinput, board):
    answer = []
    answer.append(0)
    answer.append(0)
    
    left_max, right_max = -(board[0]//2), board[0]//2
    down_max, up_max = -(board[1]//2), board[1]//2
    
    for key in keyinput:
        if (key == "left") and (answer[0]-1 >= left_max):
            answer[0] -= 1
        elif (key == "right") and (answer[0]+1 <= right_max):
            answer[0] += 1
        elif (key == "down") and (answer[1]-1 >= down_max):
            answer[1] -= 1
        elif (key == "up") and (answer[1]+1 <= up_max):
            answer[1] += 1
        else:
            continue
    
    return answer