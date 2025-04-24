import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        // 짝수 -> 0 / 홀수 -> 1
        int now = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char now_ch = s.charAt(i);
            String now_str = String.valueOf(now_ch);
            
            
            // 현재 값이 공백인 경우 -> 공백을 추가 + now를 짝수로 바꾸기
            if (now_str.equals(" ")) {
                now = 0;
                answer += " ";
                continue;
            }
            
            // 현재 값이 공백이 아닌 경우
            if (now == 1) {
                // 홀수인 경우
                answer += now_str.toLowerCase();
                now = 0;
            } else {
                // 짝수인 경우
                answer += now_str.toUpperCase();
                now = 1;
            }
            
        }
        
        
        return answer;
    }
}