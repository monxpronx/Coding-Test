# 260309

def solution(a, b, c, d):
    answer = 1
    p, q, r = 0, 0, 0
    
    num = [a, b, c, d]
    
    if len(set(num)) == 1:
        answer = a * 1111
        
    elif len(set(num)) == 4:
        answer = min(num)
    
    # (2개의 p, 1개의 q, 1개의 r)일 경우
    elif len(set(num)) == 3:
        for n in num:
            if num.count(n)==2:
                p = n
        for n in num:
            if n != p:
                q = n
        for n in num:
            if n not in [p, q]:
                r = n
        answer = q*r
                
        
    # (2개의 p와 2개의 q)일 경우
    elif len(set(num))==2 and num.count(num[1])==2:
        p = num[1]
        for n in num:
            if n != p:
                q = n
                break
        answer = (p+q) * abs(p-q)
    
    # (3개의 p, 1개의 q)일 경우
    else:
        for n in num:
            if num.count(n) == 1:
                q = n
            else:
                p = n
        answer = (10*p+q)**2
    
    return answer