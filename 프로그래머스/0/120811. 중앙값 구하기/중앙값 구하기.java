// 250719

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        int tmp;
        for(int i=0; i<array.length; i++) {
            for(int j=0; j<array.length-1-i; j++) {
                if (array[j] > array[j+1]) {
                    tmp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = tmp;
                }
            }
        } // 오름차순 버블정렬
        
        answer = array[array.length/2];
        
        return answer;
    }
}