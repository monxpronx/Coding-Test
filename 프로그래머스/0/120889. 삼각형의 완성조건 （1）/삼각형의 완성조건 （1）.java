// 250719

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        
        int max = 0, max_i = 0;
        for(int i=0; i<3; i++) {
            if (sides[i] > max) {
                max = sides[i];
                max_i = i;
            }
        } // 최댓값 갱신 코드
        
        int sum = 0;
        for(int i=0; i<3; i++) {
            if (i == max_i) continue;
            sum += sides[i];
        }  // 두 변의 합
        
        if (sum > max) answer = 1;
        else answer = 2;
        
        
        return answer;
    }
}