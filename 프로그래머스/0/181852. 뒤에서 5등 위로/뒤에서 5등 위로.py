# 260319

def solution(num_list):
    answer = []
    
    for n in num_list:
        answer.append(n)
        
    answer.sort()
    answer = answer[5:]
    
    return answer