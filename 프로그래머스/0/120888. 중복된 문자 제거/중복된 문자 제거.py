# 260130

def solution(my_string):
    answer = ''
    
    for i in range(len(my_string)): # 비교기준원소의 인덱스
        cnt = 0
        for j in range(i): # 비교대상원소의 인덱스
            if my_string[i] == my_string[j]:
                cnt += 1
                break
        if cnt == 0:
            answer += my_string[i]
    
    return answer