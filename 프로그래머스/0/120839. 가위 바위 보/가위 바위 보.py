# 260120

def solution(rsp):
    answer = ''
    
    dict1 = {
        '2': '0',
        '0': '5',
        '5': '2'
    } # 이기는 값을 딕셔너리로 정의
    
    for rs in rsp:
        answer += dict1[rs]
    
    return answer