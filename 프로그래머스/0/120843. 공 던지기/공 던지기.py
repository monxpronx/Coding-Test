# 260123

def solution(numbers, k):
    answer = 1
    cnt = 1
    
    while cnt < k:
        if answer == len(numbers)-1:
            answer = 1
        elif answer == len(numbers):
            answer = 2
        else:
            answer += 2
        cnt += 1
    
    return answer