# 260305

def solution(n, control):
    answer = 0
    
    for ch in control:
        if ch=='w':
            n+=1
        elif ch=='s':
            n-=1
        elif ch=='d':
            n+=10
        else:
            n-=10
            
        answer = n
    
    return answer