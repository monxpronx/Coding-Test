// 250719

class Solution {
    public int[] solution(int money) {
        int[] answer = {};
        
        answer = new int[2];
        answer[0] = money/5500;
        answer[1] = money - (5500*answer[0]);
        
        return answer;
    }
}