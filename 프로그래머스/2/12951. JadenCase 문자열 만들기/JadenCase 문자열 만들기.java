import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        boolean prev_blank = true;
        
        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            
            // 현재가 공백인 경우
            if (now == ' ') {
                answer += ' ';
                prev_blank = true;
                continue;
            }
            
            // 공백이 아닌 경우
            if (prev_blank == true) {
                // 지금이 단어의 첫번째 글자인 경우
                answer += Character.toUpperCase(now);
                prev_blank = false;
            } else {
                // 지금이 단어의 첫번째 글자가 아닌 경우
                answer += Character.toLowerCase(now);
            }
            
            
            
        }
        
        return answer;
    }
}