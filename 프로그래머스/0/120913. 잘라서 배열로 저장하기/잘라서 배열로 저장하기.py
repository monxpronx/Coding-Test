# 251125

def solution(my_str, n):
    answer = []
    
    cnt=0
    str=''
    for ch in my_str:
        
        if cnt==n:
            answer.append(str) # 지금까지의 문자열은 answer에 추가
            str = '' # 새로운 문자열 생성
            cnt=0 # 카운트 초기화
        
        str += ch
        cnt+=1
        
    answer.append(str)
    
    return answer