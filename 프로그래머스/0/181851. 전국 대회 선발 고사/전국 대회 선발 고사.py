# 260319

def solution(rank, attendance):
    answer = 0
    
    idx = []
    rank_num = 1
    
    while len(idx) < 3:
        for i in range(len(rank)):
            if rank[i]==rank_num:
                if attendance[i]==True:
                    idx.append(i) # idx리스트에 그 인덱스 추가
                rank_num+=1

    answer = idx[0]*10000 + idx[1]*100 + idx[2]        
        
    return answer