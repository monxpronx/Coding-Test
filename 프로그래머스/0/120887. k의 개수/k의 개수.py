# 260225

def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        temp = str(num)
        for ch in temp:
            if ch == str(k):
                answer += 1
    
    return answer