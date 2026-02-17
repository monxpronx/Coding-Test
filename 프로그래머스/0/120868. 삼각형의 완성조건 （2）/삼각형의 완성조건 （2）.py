# 260217

def solution(sides):
    answer = 0
    
    max_l = max(sides)
    min_l = min(sides)
    
    # max_l보다 길지 않은 변일 경우
    for i in range(1, max_l+1):
        if i + min_l > max_l:
            answer+=1
            
    # 가장 긴 변일 경우
    for i in range(min_l+max_l, max_l, -1):
        if max_l + min_l > i:
            answer+=1
    
    return answer