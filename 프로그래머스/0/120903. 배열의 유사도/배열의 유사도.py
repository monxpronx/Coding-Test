# 260205

def solution(s1, s2):
    answer = 0
    
    for str1 in s1: ### 비교기준원소 str1
        for str2 in s2: ### 비교대상원소 str2
            if str1 == str2:
                answer += 1
    
    return answer