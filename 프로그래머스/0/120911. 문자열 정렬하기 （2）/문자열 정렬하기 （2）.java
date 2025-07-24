// 250724

class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for(int i=0; i<my_string.length(); i++) {
            char ch = my_string.charAt(i);
            if ('A'<=ch && ch<='Z') {
                answer += (char)(ch-'A' + 'a');
            } // 대문자일 경우, 소문자로 변경해서 저장
            else answer += ch; // 소문자일 경우 그냥 저장
        }
        
        
        StringBuilder sb = new StringBuilder(answer);
        
        for(int i=0; i<sb.length(); i++) {
            for(int j=0; j<sb.length()-i-1; j++) {
                if (sb.charAt(j) > sb.charAt(j+1)) {
                    char tmp = sb.charAt(j);
                    sb.setCharAt(j, sb.charAt(j+1));
                    sb.setCharAt(j+1, tmp);
                }
            }
        } // 오름차순 버블정렬
        
        answer = sb.toString();
        
        return answer;
    }
}