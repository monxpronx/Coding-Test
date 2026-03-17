# 260317

def solution(arr, k):
    answer = []
    
    for num in arr:
        if num not in answer:
            answer.append(num)
        if len(answer)==k:
            break
            
    cnt = k-len(answer)
    for i in range(cnt):
        answer.append(-1)
    
    return answer