# 260315

def solution(myString, pat):
    answer = ''
    
    len1 = len(myString) # 7
    len2 = len(pat) # 2
    
    for i in range(len1-len2+1): # i: 0~5
        cnt = 0
        for j in range(len2):
            if myString[i+j]==pat[j]:
                cnt+=1
            else:
                break
        if cnt==len2:
            answer = '' + myString[:i+len2]
    
    return answer