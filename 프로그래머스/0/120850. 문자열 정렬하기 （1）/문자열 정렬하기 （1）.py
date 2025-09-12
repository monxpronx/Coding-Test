# 250912

def solution(my_string):
    answer = []
    
    for ch in my_string:
        if '0' <= ch <= '9':
            answer.append(int(ch))
    answer.sort()
    
    return answer