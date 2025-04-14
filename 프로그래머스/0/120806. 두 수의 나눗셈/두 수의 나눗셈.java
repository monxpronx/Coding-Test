// 250411

class Solution {
    public int solution(int num1, int num2) {
        
        double ans1;
        int ans2;
        
        ans1 = ((double)num1/num2)*1000;
        ans2 = (int)ans1;
        
        return ans2;
    }
}

// int형 변수 앞에 형변환연산자 (double)을 붙여 소수형으로 계산
// double형 변수 앞에 형변환연산자 (int)를 붙여 소수점 버리기