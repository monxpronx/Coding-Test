// 250723

class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        
        StringBuilder sb = new StringBuilder(my_string);
        
        char tmp = sb.charAt(num1);
        sb.setCharAt(num1, sb.charAt(num2));
        sb.setCharAt(num2, tmp);
        
        answer += sb.toString();
        
        return answer;
    }
}