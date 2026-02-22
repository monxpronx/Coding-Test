# 260222

def solution(babbling):
    answer = 0
        
    for babb in babbling:
        i = 0
        flag = 0
        while i < len(babb):
            if babb[i:i+3] == "aya":
                i+=3
            elif babb[i:i+2] == "ye":
                i+=2
            elif babb[i:i+3] == "woo":
                i+=3
            elif babb[i:i+2] == "ma":
                i+=2
            else:
                flag = 1
                break
            
        if flag == 0:
            answer+=1
    
    return answer