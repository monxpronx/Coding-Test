# 260303

def solution(my_string, overwrite_string, s):
    answer = ''
    
    # 앞쪽 문자열
    answer += my_string[:s]
        
    # 덮어쓸 부분
    answer += overwrite_string

    # 뒤쪽 문자열
    if len(my_string) > s+len(overwrite_string):
        answer += my_string[s+len(overwrite_string):]
    
    return answer