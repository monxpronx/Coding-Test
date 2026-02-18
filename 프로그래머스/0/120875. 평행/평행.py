# 260218

def solution(dots):
    answer = 0
    
    def isParallel(d1, d2, d3, d4):
        result = 0
        if (d2[1]-d1[1]) / (d2[0]-d1[0]) == (d4[1]-d3[1]) / (d4[0]-d3[0]):
            result = 1
        return result
    
    if isParallel(dots[0], dots[1], dots[2], dots[3]) == 1:
        answer = 1
    if isParallel(dots[0], dots[2], dots[1], dots[3]) == 1:
        answer = 1
    if isParallel(dots[0], dots[3], dots[1], dots[2]) == 1:
        answer = 1
    
    return answer