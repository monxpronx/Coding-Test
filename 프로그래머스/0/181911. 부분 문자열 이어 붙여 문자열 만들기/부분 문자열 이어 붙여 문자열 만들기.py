# 260308

def solution(my_strings, parts):
    answer = ''
    
    cnt = len(parts)
    
    for i in range(cnt):
        string = my_strings[i]
        p = parts[i]
        answer += string[p[0]:p[1]+1]
    
    return answer