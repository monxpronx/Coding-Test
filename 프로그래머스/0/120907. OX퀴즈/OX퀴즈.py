# 260207

def solution(quiz):
    answer = []
    
    for q_str in quiz:
        
        q = q_str.split()
        
        num1 = int(q[0])
        num2 = int(q[2])
        num3 = int(q[4])
        
        if (q[1] == '+') and (num1 + num2 == num3):
            answer.append('O')
        elif (q[1] == '-') and (num1 - num2 == num3):
            answer.append('O')
        else:
            answer.append('X')
            
    return answer