# 260415

def solution(n):
    
    str_n = str(n)
    list_n = list(str_n)
    list_n.sort(reverse=True)
    
    answer = ""
    for ch in list_n:
        answer += ch
        
    answer = int(answer)
    
    return answer