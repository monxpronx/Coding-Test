// 250719

class Solution {
    public int[] solution(int n, int[] numlist) {
        int[] answer = {};
        
        int cnt=0;
        for(int i=0; i<numlist.length; i++) {
            if (numlist[i] % n == 0) cnt++;
        } // 만들 answer배열의 크기를 먼저 구함
        
        answer = new int[cnt];
        
        int j = 0;
        for(int i=0; i<numlist.length; i++) {
            if (numlist[i] % n == 0) {
                answer[j++] = numlist[i];
            }
        } // answer배열에 다시 그 원소 넣기
        
        return answer;
    }
}