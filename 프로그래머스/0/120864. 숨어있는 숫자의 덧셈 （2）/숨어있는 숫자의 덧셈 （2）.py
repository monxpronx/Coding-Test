# 251124

def solution(my_string):
    answer = 0
    
    num=""
    for ch in my_string:
        if ch.isdigit():
            num+=ch
        else:
            if num!="":
                answer += int(num)
                num=""
    
    # 예외처리 (숫자로 끝난 경우)
    if num != "":
        answer += int(num)
            
    return answer