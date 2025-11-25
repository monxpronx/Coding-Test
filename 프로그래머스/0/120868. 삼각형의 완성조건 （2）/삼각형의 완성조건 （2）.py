# 251125

def solution(sides):
    answer = 0
    last_side = []
    
    max_side = max(sides)
    min_side = min(sides)    
    
    # max_side가 가장 긴 변일 경우
    for i in range(1, max_side+1):
        if max_side < min_side + i:
            last_side.append(i)
    
    # 다른 하나가 가장 긴 변일 경우
    for i in range(max_side+1, 1001+max_side):
        if i < max_side + min_side:
            last_side.append(i)
            
    last_side = list(set(last_side))
    answer = len(last_side)

    return answer