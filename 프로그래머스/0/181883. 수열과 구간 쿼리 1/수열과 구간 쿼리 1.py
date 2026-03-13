# 260313

def solution(arr, queries):
    answer = []
    
    for q in queries:
        s = q[0]
        e = q[1]
        for j in range(s, e+1):
            arr[j] += 1
            
    answer = arr
    
    return answer