// 너비우선탐색 BFS

import java.util.*;

class Solution {
    public int BFS(int[] numbers, int target) {
        int result = 0;
        Queue<int[]> q = new LinkedList<int[]>();
        q.offer(new int[] {numbers[0], 0});  // {지금까지의 합, depth}
        q.offer(new int[] {-numbers[0], 0});
        
        while (q.size() != 0) {
            int[] now = q.poll();
            int now_sum = now[0];
            int now_depth = now[1];
            
            // 마지막 depth까지 왔을 때, target에 해당하는 값이면 result += 1
            if (now_depth == numbers.length - 1) {
                if (now_sum == target) {
                    result += 1;
                }
                continue;
            }
            
            // 마지막 depth 아닌 경우 -> q에 추가
            q.offer(new int [] {now_sum + numbers[now_depth + 1], now_depth + 1});
            q.offer(new int [] {now_sum - numbers[now_depth + 1], now_depth + 1});
            
        }
        
        return result;
    }
    
    public int solution(int[] numbers, int target) {
        int answer = BFS(numbers, target);
        return answer;
    }
}