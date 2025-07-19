// 250719

class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        
        int cnt, memo_i;
        answer = 2;
        
        for(int i=0; i<=str1.length()-str2.length(); i++) { // i로 str1을 훑음
            cnt = 0;
            memo_i = i;
            for(int j=0; j<str2.length(); j++, i++) { // j로 str2를 훑음
                if (str1.charAt(i) == str2.charAt(j)) cnt++;
            }
            if (cnt==str2.length()) {
                    answer=1;
                    break;
                }
            i = memo_i;
        }
        
        return answer;
    }
}