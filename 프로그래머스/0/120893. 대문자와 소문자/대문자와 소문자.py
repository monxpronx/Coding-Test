# 251122

def solution(my_string):
    answer = ''
    
    for i in range(len(my_string)):
        if 'A'<=my_string[i]<='Z':
            answer += my_string[i].lower()
        else:
            answer += my_string[i].upper()
    
    return answer