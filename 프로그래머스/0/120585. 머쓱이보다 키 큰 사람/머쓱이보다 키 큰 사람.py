# 251119

def solution(array, height):
    answer = 0
    
    array.sort(reverse=True)
    for i in array:
        if i <= height:
            break
        answer+=1
    
    return answer