// [1, 2, 4] [4, 4, 5]
// 5 + 8 + 16 = 29

import java.util.*;

class Solution {
    public int solution(int []A, int []B) {
        int answer = 0;
        int total = A.length;
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        for (int i = 0; i < total; i++) {
            int A_num = A[i];
            int B_num = B[total - i - 1];
            
            answer += (A_num * B_num);
        }
        

        return answer;
    }
}