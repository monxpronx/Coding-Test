# 260213

def solution(dots):
    answer = 0
    min_x, min_y, max_x, max_y = 257, 257, -257, -257
    
    for i in range(4):
        if dots[i][0] > max_x:
            max_x = dots[i][0]
        if dots[i][0] < min_x:
            min_x = dots[i][0]
            
    for j in range(4):
        if dots[j][1] > max_y:
            max_y = dots[j][1]
        if dots[j][1] < min_y:
            min_y = dots[j][1]
    
    answer = (max_x-min_x) * (max_y-min_y)
    
    return answer