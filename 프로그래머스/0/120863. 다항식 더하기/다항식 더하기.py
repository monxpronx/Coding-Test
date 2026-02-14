# 260214

def solution(polynomial):
    answer = ''
    coef = 0
    cons = 0
    
    list1 = polynomial.split()
    
    for loaf in list1:
        if loaf == 'x': ### 그냥 x일 때
            coef += 1
        elif 'x' in loaf: ### x항일 때
            coef += int(loaf[:len(loaf)-1])
        elif loaf.isdigit(): ### 상수일 때
            cons += int(loaf)
        else: ### 덧셈일 떄
            continue
            
    # 정답 문자열(answer) 만들기
    if coef==0:
        answer += str(cons)
    elif coef==1 and cons==0:
        answer += ("x")
    elif coef==1 and cons!=0:
        answer += ("x + " +str(cons))
    elif cons==0:
        answer += (str(coef)+"x")
    else:
        answer += (str(coef)+"x + " + str(cons))
    
    return answer