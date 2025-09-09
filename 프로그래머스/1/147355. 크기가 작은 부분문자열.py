def solution(t, p):
    answer=0
    
    m = len(p)
    target = p

    # 같은 길이끼리의 비교는 문자열 사전순 비교 == 숫자 크기 비교와 동일
    for i in range(len(t) - m + 1):
        if t[i:i+m] <= target:
            answer += 1
    return answer
