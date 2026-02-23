# 260223

def solution(id_pw, db):
    answer = ''
    cnt_id = 0
    flag = 0
    
    for data in db:
        if (id_pw[0]==data[0]) and (id_pw[1]==data[1]):
            flag = 1
            break
        elif (id_pw[0]==data[0]) and (id_pw[1]!=data[1]):
            cnt_id += 1
        
    if flag==1:
        answer += "login"
    elif (cnt_id > 0) and (flag == 0):
        answer += "wrong pw"
    else:
        answer += "fail"
    
    return answer