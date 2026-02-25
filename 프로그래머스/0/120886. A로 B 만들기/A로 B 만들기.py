# 260225

def solution(before, after):
    answer = 1
    
    for ch in after:
        
        # 그 원소가 before의 몇 개인지 확인
        cnt1 = 0
        for ch1 in before:
            if ch1 == ch:
                cnt1 += 1
                
        # 그 원소가 after에 몇 개인지 확인
        cnt2 = 0
        for ch2 in after:
            if ch2 == ch:
                cnt2 += 1
        
        # 판별
        if cnt1 < cnt2:
            answer = 0
            break
    
    return answer