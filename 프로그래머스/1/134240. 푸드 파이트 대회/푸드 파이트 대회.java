// 1번 음식 : 3개 -> 2개
// 2번 음식 : 4개
// 3번 음식 : 6개
// total_len = (2+4+6) + 1

class Solution {
    public String solution(int[] food) {
        String answer = "";
        
        String result = "";
        for (int i = 1; i < food.length; i++) {
            int cnt = food[i] / 2;
            
            // i를 int -> char
            char food_i_char = (char) (i + '0');
            
            for (int j = 0; j < cnt; j++) {
                // i는 food 번호
                // j는 i의 개수
                
                result += food_i_char;
            }
        }
        
        // result를 기반으로 answer 만들기
        String result_reversed = "";
        
        for (int i = 0; i < result.length(); i++) {
            int idx = result.length() - i - 1;
            char now = result.charAt(idx);
            result_reversed += now;
        } 
        
        answer = result + "0" + result_reversed;
        
        return answer;
    }
}