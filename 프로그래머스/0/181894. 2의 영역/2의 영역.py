# 260312

def solution(arr):
    answer = []
    start_point, end_point = -1, -1
    flag = 0
    
    for i in range(len(arr)):
        if flag == 0 and arr[i] == 2:
            start_point = i
            flag = 1
            continue
        if flag == 1 and arr[i] == 2:
            end_point = i
        
    if start_point == -1:
        answer.append(-1)
    elif start_point != -1 and end_point == -1:
        answer.append(2)
    else:
        answer = arr[start_point:end_point+1]
    
    return answer