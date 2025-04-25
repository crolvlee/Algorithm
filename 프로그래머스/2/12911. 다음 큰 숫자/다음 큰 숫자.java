// 1001110 (78)
// 1010011 (83)

// 15 / 2 = 7 ... 1
// 7  / 2 = 3 ... 1
// 3  / 2 = 1 ... 1

//  1111 (15)
// 10111 (1 + 2 + 4 + 16 = 23)

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String str = Integer.toBinaryString(n);
        
        // 1. 1인 비트가 몇개인지 확인
        int one_cnt = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '1') {
                one_cnt += 1;
            }
        }
        
        // 2. (n+1) ~ 1000000 까지 돌면서 1인 비트의 수가 one_cnt인 것 찾기
        for (int i = (n+1); i < 1000001; i++) {
            // now_num_str: 현재 수 i를 2진수로 한 것
            String now_num_str = Integer.toBinaryString(i);
            
            int now_one_cnt = 0;
            for (int j = 0; j < now_num_str.length(); j++) {
                if (now_num_str.charAt(j) == '1') {
                    now_one_cnt += 1;
                }
            }
            
            if (now_one_cnt == one_cnt) {
                answer = i;
                break;
            }
        }
        
        
        
        return answer;
    }
}