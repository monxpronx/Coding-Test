# 260219

def solution(lines):
    answer = 0
    
    dots1, dots2, dots3 = [], [], []
    
    for i in range(lines[0][0], lines[0][1]):
        dots1.append(i)
    for i in range(lines[1][0], lines[1][1]):
        dots2.append(i)
    for i in range(lines[2][0], lines[2][1]):
        dots3.append(i)
        
    min_dot = min(lines[0][0], lines[1][0], lines[2][0])
    max_dot = max(lines[0][1], lines[1][1], lines[2][1]) + 1
    
    for dot in range(min_dot, max_dot):
        temp = 0
        if dot in dots1:
            temp+=1
        if dot in dots2:
            temp+=1
        if dot in dots3:
            temp+=1
        
        if temp >= 2:
            answer+=1
    
    return answer