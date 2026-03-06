# 260306

def solution(arr, queries):
    answer = []
    
    for i in range(len(arr)):
        answer.append(arr[i])
    
    for q in queries:
        s = q[0]
        e = q[1]
        k = q[2]
        for i in range(s, e+1):
            if i%k==0:
                answer[i] += 1
    
    return answer