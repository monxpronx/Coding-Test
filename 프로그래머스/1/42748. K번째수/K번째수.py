# 260330

def solution(array, commands):
    answer = []
    
    for c in commands:
        tmp = []
        i, j, k = c[0], c[1], c[2]
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    
    return answer