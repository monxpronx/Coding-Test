# 260321

def solution(arr, k):
    answer = []
    
    if k%2==1:
        for n in arr:
            answer.append(n*k)
    else:
        for n in arr:
            answer.append(n+k)
    
    return answer