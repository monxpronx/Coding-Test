# 260319

def solution(num_str):
    answer = 0
    
    num = []
    for ch in num_str:
        num.append(int(ch))
    answer = sum(num)
    
    return answer