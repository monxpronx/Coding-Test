# 250910

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
            if n%i==0 and n/i<=1000000:
                answer+=1
    
    return answer