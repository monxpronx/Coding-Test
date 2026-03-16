# 260316

def solution(myString):
    answer = []
    
    tmp = myString.split("x")
    while "" in tmp:
        tmp.remove("")
    answer = sorted(tmp)
    
    return answer