// 250724

class Solution {
    public int solution(int num, int k) {
        int answer = 0;
        
        int N=num, cnt=0;
        while (N>0) {
            N/=10;
            cnt++;
        } // 자릿수 세기
        
        int[] number = new int[cnt];
        
        for(int i=cnt-1; i>=0; i--) {
            number[i] = num%10;
            num/=10;
        } // 숫자를 배열에 저장
        
        answer = -1;
        for(int i=0; i<cnt; i++) {
            if (number[i] == k) {
                answer = i+1;
                break;
            }
        }
        
        return answer;
    }
}