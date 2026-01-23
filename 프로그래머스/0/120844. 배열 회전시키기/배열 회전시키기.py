# 260123

def solution(numbers, direction):
    answer = []
    
    if direction == "right":
        tmp = numbers[len(numbers)-1]
        answer.append(tmp)
        answer.extend(numbers[:len(numbers)-1])
    else:
        tmp = numbers[0]
        answer.extend(numbers[1:])
        answer.append(tmp)
        
    return answer