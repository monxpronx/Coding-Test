# 260324

def solution(participant, completion):
    answer = ''
    
    ### 딕셔너리 제작
    count = {}
    for p in participant:
        if p not in count:
            count[p] = 1
        else:
            count[p] += 1
    
    # count의 개수 소거
    for c in completion:
        count[c] -= 1
    
    # 정답 찾기
    for c in count:
        if count[c] != 0:
            answer += c
            break
    
    return answer