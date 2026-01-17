# 260117

def solution(emergency):
    answer = []
    
    for emer1 in emergency: # 비교기준원소 emer1
        cnt=1
        for emer2 in emergency: # 비교대상원소 emer2
            if emer1 < emer2:
                cnt+=1
        answer.append(cnt)
    
    return answer