# 260204

def solution(array):
    answer = []
    max = 0
    max_i = 0
    
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            max_i = i
    
    answer.append(max)
    answer.append(max_i)
    
    return answer