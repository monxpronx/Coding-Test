// 250719

class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        
        int cnt;
        if (n%2==0) cnt = n/2;
        else cnt = n/2+1;
        answer = new int[cnt];
        
        int i=0;
        for(int j=1; j<=n; j+=2) {
            answer[i++] = j;
        }
        
        return answer;
    }
}