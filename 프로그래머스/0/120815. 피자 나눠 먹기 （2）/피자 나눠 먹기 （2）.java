// 250724

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(answer=1; ; answer++) {
            if ((6*answer)%n == 0) break;
        }
        
        return answer;
    }
}