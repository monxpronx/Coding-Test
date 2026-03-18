# 260318

def solution(arr, n):
    answer = []
    
    for num in arr:
        answer.append(num)
    
    if len(answer)%2==1:
        for i in range(0, len(answer), 2):
            answer[i] += n
    else:
        for i in range(1, len(answer), 2):
            answer[i] += n
    
    return answer