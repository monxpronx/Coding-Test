// 250719

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        
        answer = new int[numbers.length];
        for(int i=0; i<numbers.length; i++) {
            answer[i] = numbers[i]*2;
        }
        
        return answer;
    }
}