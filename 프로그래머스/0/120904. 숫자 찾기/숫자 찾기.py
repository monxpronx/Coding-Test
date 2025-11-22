# 251122

def solution(num, k):
    answer = -1
    
    str_num = str(num) # 문자열로 변경
    str_k = str(k)
    
    for i in range(len(str_num)):
        if str_k == str_num[i]:
            answer = i+1
            break
    
    return answer