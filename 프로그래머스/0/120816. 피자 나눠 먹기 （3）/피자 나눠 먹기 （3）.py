# 260108

def solution(slice, n):
    answer = 0
    
    while 1:
        if slice * answer >= n:
            break
        answer += 1
    
    return answer