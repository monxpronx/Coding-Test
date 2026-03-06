# 260306

def solution(x1, x2, x3, x4):
    answer = True
    
    tmp1 = x1 or x2
    tmp2 = x3 or x4
    answer = tmp1 and tmp2
    
    return answer