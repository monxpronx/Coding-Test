# 260416

def solution(x, n):
    answer = []
    
    cnt = 0
    tmp = x
    while cnt < n:
        answer.append(tmp)
        tmp += x
        cnt += 1
    
    return answer