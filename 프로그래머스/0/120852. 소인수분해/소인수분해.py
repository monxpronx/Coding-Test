# 260128

def solution(n):
    answer = []
    
    for num in range(2, n+1):
        if n % num == 0:
            cnt = 0
            for i in range(2, num):
                if num%i==0:
                    cnt+=1
            if cnt==0 and num not in answer:
                answer.append(num)
    
    answer.sort()
    
    return answer