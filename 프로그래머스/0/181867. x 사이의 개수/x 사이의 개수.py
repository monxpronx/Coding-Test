# 260316

def solution(myString):
    answer = []
    
    tmp = myString.split("x")
    for t in tmp:
        answer.append(len(t))
    
    return answer