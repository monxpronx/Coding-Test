# 251125

def solution(n):
    answer = []
    
    i=2 # 2부터 시작
    while i * i <= n: # 소인수 구할 때 조건식 (그냥 알아두기) 
        if n%i==0:
            answer.append(i)
            while n%i==0:
                n //= i
        i+=1
    
    if n>1:
        answer.append(n)

    return answer