// 250410

class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        double ans;
        
        ans = ((double)num1/num2)*1000;
        answer = (int)ans;
        
        return answer;
    }
}

// int형 변수 앞에 형변환연산자 (double)을 붙여 소수형으로 계산
// double형 변수 앞에 형변환연산자 (int)를 붙여 소수점 버리기