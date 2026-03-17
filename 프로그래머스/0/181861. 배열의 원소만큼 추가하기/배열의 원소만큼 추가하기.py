# 260317

def solution(arr):
    answer = []
    
    for num in arr:
        for i in range(int(num)):
            answer.append(int(num))
    
    return answer