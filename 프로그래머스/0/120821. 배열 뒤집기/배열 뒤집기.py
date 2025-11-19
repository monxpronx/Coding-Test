# 251119

def solution(num_list):
    answer = []
    
    answer = list(reversed(num_list))
    
    return answer


'''
리스트를 뒤집는 방법 3가지

1) [::-1] 슬라이싱
-> 리스트의 크기가 매우 클 경우, 메모리 과다사용 위험

2) reversed() 메소드
-> 반환값이 이터레이터이므로, list()로 감싸줘야함

3) reverse() 함수
-> 그냥 num_list가 뒤집어질 뿐 (원래 리스트 복원 불가능)


'''