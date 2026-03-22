# 260322

def solution(arr):
    answer = []
    
    l1 = len(arr) # 행 수
    l2 = len(arr[0]) # 열 수
    
    for i in range(l1):
        answer.append([])
        for j in range(l2):
            answer[i].append(arr[i][j])
    
    if l2 < l1: # 행이 더 많을 떄
        for i in range(l1):
            for j in range(l1-l2):
                answer[i].append(0)
    else: # 열이 더 많을 떄
        for i in range(l2-l1):
            answer.append([])
            for j in range(l2):
                answer[l1+i].append(0)
    
    return answer