# 260318

def solution(strArr):
    answer = 0
    length = [0]*31
    
    for string in strArr:
        i = len(string)
        length[i]+=1
        
    answer = max(length)
    
    return answer