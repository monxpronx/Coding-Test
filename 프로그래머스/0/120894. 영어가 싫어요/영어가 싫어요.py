# 251125

def solution(numbers):
    answer = 0
    
    num_map = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
               "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for word, digit in num_map.items():
        # 딕셔너리.items(): (key,value) 쌍을 하나씩 꺼냄
        numbers = numbers.replace(word,digit)
    
    answer =int(numbers)
    
    return answer