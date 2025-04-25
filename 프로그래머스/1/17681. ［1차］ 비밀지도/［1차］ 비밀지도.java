import java.util.*;

// 10진수 -> 2진수

// 30을 11110으로
// 30 / 2 = 15 ... 0
// 15 / 2 = 7  ... 1
// 7  / 2 = 3  ... 1
// 3  / 2 = 1  ... 1

// 1을 1로
// 1  / 2 = 0  ... 1

    
class Solution {
    public String getBinary(int num, int n) {
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            sb.append(0);
        }
        
        // 10진수(int) -> 2진수(String)
        // ex. 30 -> 01001
        int now_num = num;
        int now_idx = n - 1;
        
        while (true) {
            if (now_num / 2 == 0) {
                int rest = now_num % 2;
                char rest_ch = (char) (rest + '0');
                sb.setCharAt(now_idx, rest_ch);
                break;
                
            } else if (now_num / 2 == 1) {
                int rest = now_num % 2;
                char rest_ch = (char) (rest + '0');
                sb.setCharAt(now_idx, rest_ch);
                sb.setCharAt(now_idx - 1, '1');
                break;
            } else {
                int rest = now_num % 2;     // 나머지
                char rest_ch = (char) (rest + '0');
                sb.setCharAt(now_idx, rest_ch);
                
                now_num = now_num / 2;
                now_idx -= 1;
            }
        }
        
        return sb.toString();
    }
    
    public String[] solution(int n, int[] arr1, int[] arr2) {
            
        // arr1 배열 -> 배열 ground1 만들기
        String[] ground1 = new String[n];
        for (int i = 0; i < n; i++) {
            String now_line = getBinary(arr1[i], n);
            ground1[i] = now_line;
        }
        
        // arr2 배열 -> 배열 ground2 만들기
        String[] ground2 = new String[n];
        for (int i  = 0; i < n; i++) {
            String now_line = getBinary(arr2[i], n);
            ground2[i] = now_line;
        }
        
        // ground1과 ground2를 바탕으로 -> answer 배열 만들기
        String[] answer = new String[n];
        
        for (int i = 0; i < n; i++) {
            String line = "";
            String first_line = ground1[i];
            String second_line = ground2[i];
                
            for (int j = 0; j < n; j++) {
                char first_char = first_line.charAt(j);
                char second_char = second_line.charAt(j);
                
                if (first_char == '1' || second_char == '1') {
                    line += '#';
                } else {
                    line += ' ';
                }
            }
            
            answer[i] = line;
        }
        
        
        
        return answer;
    }
}