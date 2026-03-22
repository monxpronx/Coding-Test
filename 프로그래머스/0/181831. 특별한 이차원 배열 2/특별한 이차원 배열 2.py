# 260322

def solution(arr):
    answer = 1
    flag = 1
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                answer = 0
                flag = 0
                break
        if flag == 1:
            break
    
    return answer