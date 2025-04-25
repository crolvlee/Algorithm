import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] arr_s = s.split(" ");
        
        // String 배열 -> int배열
        int[] arr = new int[arr_s.length];
        
        for (int i = 0; i < arr_s.length; i++) {
            String now_s = arr_s[i];
            char first = now_s.charAt(0);
            if (first == '-') {
                // 음수인 경우
                int now = -Integer.parseInt(now_s.substring(1));
                arr[i] = now;
            } else {
                // 양수인 경우
                int now = Integer.parseInt(now_s);
                arr[i] = now;
            }
        }
        
        // max 찾기 / min 찾기
        int max_num = Integer.MIN_VALUE;
        int min_num = Integer.MAX_VALUE;
        
        for (int i = 0; i < arr.length; i++) {
            int now_num = arr[i];
            
            if (now_num >= max_num) {
                max_num = now_num;
            }
            if (now_num <= min_num) {
                min_num = now_num;
            }
        }
        
        String min_num_s = String.valueOf(min_num);
        String max_num_s = String.valueOf(max_num);
        answer = min_num + " " + max_num;
        
        return answer;
    }
}