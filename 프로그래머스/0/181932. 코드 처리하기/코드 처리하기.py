# 260305

def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        
        if mode == 0: ### mode=0 일 때
            if code[i]!='1' and i%2==0:
                answer += code[i]
            elif code[i]!='1' and i%2==1:
                continue
            else:
                mode = 1
                continue
                
        else: ### mode=1 일 때
            if code[i]!='1' and i%2==1:
                answer += code[i]
            elif code[i]!='1' and i%2==0:
                continue
            else:
                mode = 0
                continue
    
    if answer == "":
        answer += "EMPTY"
    
    return answer