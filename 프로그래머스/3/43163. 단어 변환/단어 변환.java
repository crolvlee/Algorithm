// 너비우선 BFS 문제!

import java.util.*;

class Solution {
    boolean[] visited;
    
    public boolean check(String before, String after) {
        boolean can_convert = false;
        int n = before.length();
        int different_cnt = 0;  // 알파벳 다른거 세기
        
        for (int i = 0; i < n; i++) {
            if (different_cnt >= 2) {
                break;
            }
            
            if (before.charAt(i) != after.charAt(i)) {
                different_cnt += 1;
            }
        }
        
        if (different_cnt == 1) {
            can_convert = true;
        }
        
        return can_convert;
    }
    
    public int BFS(String begin, String target, String[] words) {
        int result = 0;
        Queue<Object[]> q = new LinkedList<>();
        q.offer(new Object[]{begin, 0});

        while (q.size() != 0) {
            Object[] now = q.poll();
            String now_word = (String) now[0];
            int now_depth = (int) now[1];
            
            // 타겟을 찾으면
            if (now_word.equals(target)) {
                result = now_depth;
                break;
            }
            
            for (int i = 0; i < words.length; i++) {
                if (visited[i] == false) {
                    boolean can_convert = check(now_word, words[i]);
                    
                    if (can_convert == true) {
                        q.offer(new Object[] {words[i], now_depth + 1});
                        visited[i] = true;
                    }
                }
            }
            
        }
        
        return result;
    }
    
    public int solution(String begin, String target, String[] words) {
        int n = words.length;
        visited = new boolean[n];
        
        for(int i = 0; i < n; i++) {
            visited[i] = false;
        }
        
        
        int answer = BFS(begin, target, words);
        return answer;
    }
}