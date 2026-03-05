# 260305

def solution(arr, queries):
    answer = []
    
    for q in queries:
        
        s = q[0]
        e = q[1]
        k = q[2]
        flag = 0
        
        min_num = float('inf')
        for i in range(s, e+1):
            if k < arr[i] and arr[i] < min_num:
                min_num = arr[i]
                flag = 1 ### 답이 -1은 아님을 표시
        if flag == 1:
            answer.append(min_num)
        else:
            answer.append(-1)
    
    return answer