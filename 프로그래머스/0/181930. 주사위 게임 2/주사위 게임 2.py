# 260305

def solution(a, b, c):
    answer = 0
    cnt = 0
    
    if a==b:
        cnt+=1
    if b==c:
        cnt+=1
    if c==a:
        cnt+=1
        
    if cnt==0:
        answer = (a+b+c)
    elif cnt==1:
        answer = (a+b+c) * (a**2+b**2+c**2)
    else:
        answer = (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    
    return answer