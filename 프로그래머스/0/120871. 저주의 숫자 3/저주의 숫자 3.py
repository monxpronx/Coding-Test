# 260218

def solution(n):
    answer = 1
    cnt = 0
    
    while cnt < n:
        if (answer % 3 != 0) and ('3' not in str(answer)):
            cnt+=1
        if cnt==n:
            break
        answer+=1
    
    return answer