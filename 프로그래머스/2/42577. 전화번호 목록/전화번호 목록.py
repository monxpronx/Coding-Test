# 260326

def solution(phone_book):
    answer = True
    
    num = set(phone_book)
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            prefix = phone[:i]
            if prefix in num:
                answer = False
                break
            if answer == False:
                break
    
    return answer