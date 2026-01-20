# 260120

def solution(balls, share):
    answer = 1
    
    for i in range(share):
        answer *= balls
        balls = balls-1
        
    for j in range(2, share+1):
        answer //= j
    
    return answer