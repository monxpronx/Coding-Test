# 260305

def solution(arr, queries):
    answer = []
    
    for q in queries:
        i = q[0]
        j = q[1]
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        
    for num in arr:
        answer.append(num)
    
    return answer