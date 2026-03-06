# 260306

def solution(my_string, queries):
    answer = my_string
    
    for q in queries:
        s = q[0]
        e = q[1]
        tmp = '' + answer[:s]
        for i in range(e, s-1, -1):
            tmp += answer[i]
        tmp += answer[e+1:]
        answer = tmp
        
    return answer