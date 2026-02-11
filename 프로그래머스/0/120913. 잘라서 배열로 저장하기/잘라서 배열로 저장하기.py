# 260211

def solution(my_str, n):
    answer = []
    
    if len(my_str) % n == 0:
        pairs = len(my_str)//n
    else:
        pairs = len(my_str)//n + 1
    
    for i in range(pairs):
        temp = ''
        temp += my_str[n*i:n*(i+1)]
        answer.append(temp)
    
    return answer