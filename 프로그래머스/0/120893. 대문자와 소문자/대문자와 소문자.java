// 250723

class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for(int i=0; i<my_string.length(); i++) {
            char ch = my_string.charAt(i);
            if ('a' <= ch && ch <= 'z') answer += (char)('A' + (ch-'a')); // 소문자->대문자
            else answer += (char)('a' + (ch-'A')); // 대문자->소문자
        }
        
        return answer;
    }
}