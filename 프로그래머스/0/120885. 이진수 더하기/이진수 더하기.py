# 260224

def solution(bin1, bin2):
    answer = ''
    
    # 길이 맞추기
    i, j = len(bin1), len(bin2)
    if i < j:
        bin1 = '0'*(j-i) + bin1
        i = j
    else:
        bin2 = '0'*(i-j) + bin2
        j = i
        
    i -= 1
    j -= 1
    c = 0
    temp = ""
    while i>=0:
        
        if int(bin1[i]) + int(bin2[j]) + c == 3:
            temp += '1'
            c = 1
        elif int(bin1[i]) + int(bin2[j]) + c == 2:
            temp += '0'
            c = 1
        elif int(bin1[i]) + int(bin2[j]) + c == 1:
            temp += '1'
            c = 0
        else:
            temp += '0'
            c = 0    
        i -= 1
        j -= 1
    
    if c==1:
        temp += '1'
    answer = temp[::-1]
    
    return answer