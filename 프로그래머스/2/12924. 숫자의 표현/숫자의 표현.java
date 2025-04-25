// 1, 2, 3, 4, 5, 6,

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n; i++) {
            // 시작 위치를 i로 고정
            int now_sum = i;
            for (int j = i + 1; j < n; j++) {
                if (now_sum + j < n) {
                    now_sum += j;
                } else if (now_sum + j == n) {
                    now_sum += j;
                    break;
                } else {
                    break;
                }
            }
            
            if (now_sum == n) {
                answer += 1;
            }
            
        }
        
        return answer;
    }
}