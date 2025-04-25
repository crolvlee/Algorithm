// 10진법 -> 2진법
// 1     ->  01
// 2     ->  10
// 3     ->  11
// 4     -> 100
// 5     -> 101
// 6     -> 110

// 6 / 2 = 3 ... 0
// 3 / 2 = 1 ... 1

// 1 / 1 = 1 ... 0

class Solution {
    String getBinary(int num) {
        if (num == 1) {
            return "1";
        }
        
        String result = "";
        int now_num = num;
        
        while (now_num > 1) {
            if (now_num / 2 == 1) {
                int rest = now_num % 2;
                result += (char)(rest + '0');
                result += '1';
                now_num = now_num / 2;
            } else {
                int rest = now_num % 2;
                result += (char)(rest + '0');
                now_num = now_num / 2;
            }
        }
        
        // result를 거꾸로 해주기
        String binary_str = "";
        
        for (int i = 0; i < result.length(); i++) {
            int idx = result.length() - i - 1;
            binary_str += result.charAt(idx);
        }
        
        return binary_str;
    }
    
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        String now_s = s;
        int iter_cnt = 0;   // 반복 횟수
        int remove_cnt = 0; // 제거한 0의 개수
        
        while (true) {
            if (now_s.equals("1")) {
                break;
            }
            
            // 1. 1의 개수 구하기 (= 0 제거 후 길이)
            int one_cnt = 0;
            for (int i = 0; i < now_s.length(); i++) {
                if (now_s.charAt(i) == '1') {
                    one_cnt += 1;
                }
            }
            
            remove_cnt += (now_s.length() - one_cnt);
            
            // 2. one_cnt를 2진법으로 바꾸기
            String result = getBinary(one_cnt);
            
            now_s = result;
            iter_cnt += 1;
        }
        
        answer[0] = iter_cnt;
        answer[1] = remove_cnt;
        
        return answer;
    }
}