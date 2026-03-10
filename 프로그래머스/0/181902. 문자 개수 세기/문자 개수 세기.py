# 260310

def solution(my_string):    
    
    answer = [0] * 52
    
    ### ord(): 문자를 실수로 바꿔주는 함수
    for ch in my_string:
        if ord(ch) < ord('a'): # 대문자일 경우
            answer[ord(ch)-ord('A')] += 1
        else: # 소문자일 경우
            answer[26 + ord(ch)-ord('a')] += 1
    
    return answer