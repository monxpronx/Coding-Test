// 250718

class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        
        answer = (int) (((double)num1 / (double)num2) * 1000);
        
        return answer;
    }
}