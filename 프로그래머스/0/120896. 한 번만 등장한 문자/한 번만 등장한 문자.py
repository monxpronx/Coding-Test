# 260203

def solution(s):
    answer = ''
    
    for ch1 in s: ### 비교기준원소 ch1
        cnt = 0
        for ch2 in s: ### 비교대상원소 ch2
            if ch1 == ch2:
                cnt+=1
        if cnt == 1:
            answer += ch1
    answer = ''.join(sorted(answer))
    
    return answer