// 너비우선 BFS 문제

// 편의상 시작점을 0행 0열
// 맵 => 행: n / 열: m

import java.util.*;

class Solution {
    boolean[][] visited;
    
    // 동서남북
    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public int BFS(int[][] maps, int end_row, int end_col) {
        int result = 0;
        boolean found = false;
        Queue<int[]> q = new LinkedList<int[]>();
        q.offer(new int[] {0, 0, 1});    // 현재 row, 현재 col, 지나온 칸 수(depth)
        visited[0][0] = true;
        
        while (q.size() != 0) {
            int[] now = q.poll();
            int now_row = now[0];
            int now_col = now[1];
            int now_depth = now[2];
            
            // 찾았으면
            if (now_row == end_row && now_col == end_col) {
                found = true;
                result += now_depth;
                break;
            }
            
            
            // 동서남북 이동
            for (int [] direction : directions) {
                int d_row = direction[0];
                int d_col = direction[1];
                
                if ((0 <= now_row + d_row) && (now_row + d_row <= end_row) && (0 <= now_col + d_col) && (now_col + d_col <= end_col)) {
                    if (maps[now_row + d_row][now_col + d_col] == 1) {
                        if (visited[now_row + d_row][now_col + d_col] == false) {
                            q.offer(new int[] {now_row + d_row, now_col + d_col, now_depth + 1});
                            visited[now_row + d_row][now_col + d_col] = true;
                        }
                    }
                }
            }
        }
        
        if (found == true) {
            return result;
        } else {
            return -1;
        }
        
    }
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        visited = new boolean[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = false;
            }
        }
        
        // for (boolean[] line : visited) {
        //     System.out.println(Arrays.toString(line));
        // }
        
        int answer = BFS(maps, n-1, m-1);
        
        
        return answer;
    }
}