# 260106

def solution(n):
    answer = []
    
    for i in range(1,n,2):
        answer.append(i)
    
    if n%2==1:
        answer.append(n)
    
    return answer