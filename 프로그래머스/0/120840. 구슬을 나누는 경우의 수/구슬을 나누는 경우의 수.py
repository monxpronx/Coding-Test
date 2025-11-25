# 251125

def solution(balls, share):
    answer = 1
    
    cnt=0
    for i in range(balls,1,-1):
        answer *= i
        cnt+=1
        if cnt==share:
            break
            
    cnt=0
    for j in range(share,1,-1):
        answer //= j
        cnt+=1
        if cnt==share:
            break
    
    return answer