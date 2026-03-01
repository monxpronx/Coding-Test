# 260301

def solution(num, total):
    answer = []
    
    if num%2==1: # 홀수 개
        start = (total//num) - (num//2)
    else: # 짝수 개
        start = (total//num) - (num//2) + 1
        
    for i in range(start, start+num):
        answer.append(i)
    
    return answer