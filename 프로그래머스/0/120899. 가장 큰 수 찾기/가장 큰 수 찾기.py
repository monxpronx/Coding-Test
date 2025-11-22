# 251122

def solution(array):
    answer = []
    
    max = float('-inf')
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            max_i = i
            
    answer.append(max)
    answer.append(max_i)
    
    return answer