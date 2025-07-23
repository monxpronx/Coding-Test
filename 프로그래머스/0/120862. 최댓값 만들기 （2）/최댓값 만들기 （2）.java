// 250723

class Solution {
    public int solution(int[] numbers) {
        int answer = Integer.MIN_VALUE; // 0이 아닌 MIN_VALUE로 선언!
        
        for(int i=0; i<numbers.length; i++) {
            for(int j=0; j<numbers.length; j++) {
                if (i==j) continue;
                if (numbers[i] * numbers[j] > answer) answer = numbers[i] * numbers[j];
            }
        }
        
        return answer;
    }
}