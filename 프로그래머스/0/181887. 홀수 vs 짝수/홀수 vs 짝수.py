# 260313

def solution(num_list):
    answer = 0
    
    sum_odd = 0
    sum_even = 0
    
    for i in range(len(num_list)):
        if (i+1)%2==1:
            sum_odd += num_list[i]
        else:
            sum_even += num_list[i]
            
    answer = max(sum_odd, sum_even)
    
    return answer