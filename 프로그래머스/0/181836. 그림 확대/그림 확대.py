# 260321

def solution(picture, k):
    answer = []
    
    for pic in picture:
        tmp = ""
        for p in pic:
            for i in range(k):
                tmp += p
        for i in range(k):
            answer.append(tmp)
        
    
    return answer