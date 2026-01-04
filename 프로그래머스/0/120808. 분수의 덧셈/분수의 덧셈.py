# 260104

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    # 분수 덧셈
    denom = denom1 * denom2
    numer1 *= denom2
    numer2 *= denom1
    numer = numer1 + numer2
    
    # 기약분수 만들기
    for i in range(min(denom,numer)-1, 1, -1):
        if denom%i==0 and numer%i==0:
            denom = denom // i
            numer = numer // i
            
    answer.append(numer)
    answer.append(denom)
    
    return answer