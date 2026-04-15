# 260415

def solution(n):
    answer = 0
    
    x = n**0.5
    if int(x) == x:
        answer = (x+1)**2
    else:
        answer = -1
    
    return answer