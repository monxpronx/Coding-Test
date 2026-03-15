# 260315

def solution(myString, pat):
    answer = 0
    
    len1 = len(myString)
    len2 = len(pat)
    
    for i in range(len1-len2+1):
        cnt = 0
        for j in range(len2):
            if myString[i+j]==pat[j]:
                cnt+=1
            else:
                break
        if cnt==len2:
            answer+=1
    
    return answer