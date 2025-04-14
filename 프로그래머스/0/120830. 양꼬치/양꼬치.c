#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int k) {
    int answer = 0;
    int cnt;
    cnt = k - n/10;
    answer += 12000*n + 2000*cnt;
    
    
    return answer;
}