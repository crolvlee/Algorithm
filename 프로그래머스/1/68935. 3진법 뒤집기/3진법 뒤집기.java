// 45 / 3 = 15 ... 0
// 15 / 3 = 5  ... 0
// 5  / 3 = 1  ... 2

// 1 / 3 = 0  ... 1

// 10진법| 3진법
// 1    | 1

// 10진법| 2진법
// 1    | 001
// 2    | 010
// 3    | 011
// 4    | 100

// 3진법 | 10진법
// 1    |  1
// 2    |  2
// 3    |  3
// 4    | 10

import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        // n -> 앞뒤 반전 (3진법)
        List<Integer> list = new ArrayList<>();
        int now_n = n;
        while (true) {
            int x = now_n / 3;
            int y = now_n % 3;
            
            list.add(y);
            
            if (x == 0) {
                break;
            } else if (0 < x && x < 3) {
                now_n = x;
                list.add(x);
                break;
            } else {
                now_n = x;
            }
        }
        
        System.out.println("list: " + list);
        
        // 앞뒤 반전(3진법) 리스트 -> 숫자형
        String result_str = "";
        for (int num : list) {
            // int -> char
            char num_ch = (char) (num + '0');
            result_str += num_ch;
        }
        
        System.out.println("result_str: " + result_str);
        
        for (int i = 0; i < result_str.length(); i++) {
            int now_idx = result_str.length() - i - 1;
            char now_num = result_str.charAt(now_idx);
            answer += (now_num - '0') * Math.pow(3, i);
        }
        
        
        return answer;
    }
}