# 260501

def solution(t, p):
    answer = 0
    
    length1 = len(t)
    length2 = len(p)
    
    for i in range(length1-length2+1):
        tmp = t[i:i+length2]
        if int(tmp) <= int(p):
            answer += 1
    
    return answer