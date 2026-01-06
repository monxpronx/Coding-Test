# 260106

def solution(array):
    answer = 0
    mode_cnt = 0
    
    for num1 in array: # num1: 비교기준원소
        cnt=0
        for num2 in array: # num2: 비교대상원소
            if num1==num2:
                cnt+=1
        if cnt > mode_cnt:
            mode_cnt = cnt
            answer = num1
        elif cnt == mode_cnt and num1 != answer:
            answer=-1
    
    return answer