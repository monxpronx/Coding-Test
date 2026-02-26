# 260226

def solution(A, B):
    answer = -1
    length = len(A)
    
    for i in range(length):
        temp = A[length-i:] + A[:length-i]
        if temp == B:
            answer = i
            break
        
    return answer