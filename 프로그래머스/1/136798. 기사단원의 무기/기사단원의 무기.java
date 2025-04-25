// 1 -> 1            // 루트1 = 1         -> 1
// 2 -> 1, 2         // 루트2 = 1.xx      -> 1

// 4 -> 1, 2, 4
// 6 -> 1, 2, 3, 6   // 루트6 = 2.xx      -> 1~2
// 7 -> 1, 7         // 루트7 = 2.xx      -> 1~2
// 8 -> 1, 2, 4, 8   // 루트8 = 2.xx      -> 1~2
// 9 -> 1, 3, 9      // 루트9 = 3         -> 1~3


import java.util.*;

class Solution {
    // 약수의 개수를 찾는 함수
    public int getCnt(int num) {
        int result = 0;
        
        double mid_d = Math.pow(num, 0.5);      // 2.xxx // 2.0
        int mid_i = (int) mid_d;                // 2     // 2
        
        if (mid_i == mid_d) {
            // 1. 제곱수인 경우
            for (int i = 1; i < mid_i; i++) {
                if (num % i == 0) {
                    result += 1;
                }
            }
            result = result * 2 + 1;
        } else {
            // 2. 제곱수가 아닌 경우
            for (int i = 1; i <= mid_i; i++) {
                if (num % i == 0) {
                    result += 1;
                }
            }
            result = result * 2;
        }
        
        
        return result;
    }
    
    public int solution(int number, int limit, int power) {
        
        // 1부터 number까지의 약수의 개수를 list에 담기
        List<Integer> list = new ArrayList<>();
        
        for (int i = 1; i <= number; i++) {
            int now_cnt = getCnt(i);
            
            if (now_cnt <= limit) {
                list.add(now_cnt);
            } else {
                list.add(power);
            }
        }
        

        // 정답 넣기
        int answer = 0;
        for (int num : list) {
            answer += num;
        }
        
        
        return answer;
    }
}