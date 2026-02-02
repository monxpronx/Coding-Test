# 260202

def solution(numbers):
    answer = 0
    
    word_to_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    ### 문자열을 훑는게 아니라 딕셔너리를 하나씩 꺼내며 훑음!!
    for word, num in word_to_num.items():
        numbers = numbers.replace(word, str(num))
        
    answer = int(numbers)
    
    return answer