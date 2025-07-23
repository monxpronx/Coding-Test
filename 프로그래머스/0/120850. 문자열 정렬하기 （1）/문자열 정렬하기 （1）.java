// 250723

class Solution {
    public int[] solution(String my_string) {
        int[] answer = {};
        
        int cnt=0;
        for(int i=0; i<my_string.length(); i++) {
            if ('0' <= my_string.charAt(i) && my_string.charAt(i) <= '9') cnt++;
        }  // 숫자의 개수 세기
        answer = new int[cnt];
        
        int j=0;
        for(int i=0; i<my_string.length(); i++) {
            if ('0' <= my_string.charAt(i) && my_string.charAt(i) <= '9') {
                answer[j++] = my_string.charAt(i) - '0';
            }
        } // answer배열에 숫자 넣기
        
        for(int i=0; i<cnt; i++) {
            for(j=0; j<cnt-i-1; j++) {
                if (answer[j] > answer[j+1]) {
                    int tmp = answer[j];
                    answer[j] = answer[j+1];
                    answer[j+1] = tmp;
                }
            }
        } // 오름차순 버블정렬
        
        return answer;
    }
}