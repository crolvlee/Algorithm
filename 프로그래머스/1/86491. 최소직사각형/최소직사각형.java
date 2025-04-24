import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int total = sizes.length;
        
        // 제일 긴 길이 하나 정하기
        int max_num = 0;
        for (int i = 0; i < total; i++) {
            if (sizes[i][0] < sizes[i][1]) {
                if (max_num < sizes[i][1]) {
                    max_num = sizes[i][1];
                }
            } else {
                if (max_num < sizes[i][0]) {
                    max_num = sizes[i][0];
                }
            }
        }
        
        // 짧은 쪽의 길이를 담는 리스트
        List<Integer> list = new ArrayList<>();
        
        // 한 번씩 돌면서 짧은 길이 쪽에 들어갈 것들을 list에 담기
        for (int i = 0; i < total; i++) {
            int min_num = 0;
            
            if (sizes[i][0] < sizes[i][1]) {
                min_num = sizes[i][0];
            } else {
                min_num = sizes[i][1];
            }
            
            list.add(min_num);
        }
        
        // list에서 가장 큰 값을 찾기
        int other_num = Collections.max(list);
        
        // 정답
        int answer = max_num * other_num;
        
        return answer;
    }
}