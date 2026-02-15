# 260215

def solution(my_string):
    answer = 0
    temp = ""
    
    for ch in my_string:
        if ch.isdigit(): # 숫자일 때
            temp += ch
        else: # 문자일 때
            if temp!="":
                answer += int(temp)
                temp = ""
                
    if temp != "": ### 숫자로 끝났을 경우
        answer += int(temp)
            
    
    return answer