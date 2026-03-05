# 260305

def solution(numLog):
    answer = ''
    
    for i in range(len(numLog)-1):
        
        j = i+1
        diff = numLog[j] - numLog[i]
        
        if diff == 1:
            answer+='w'
        elif diff == -1:
            answer+='s'
        elif diff == 10:
            answer+='d'
        else:
            answer+='a'
    
    return answer