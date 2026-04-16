# 260416

def solution(x):
    answer = True
    total = 0
    
    str_x = str(x)
    list_x = list(str_x)
    for ch in list_x:
        total += int(ch)

    if x % total != 0:
        answer = False
    
    return answer