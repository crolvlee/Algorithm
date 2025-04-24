import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int idx = 0; idx < commands.length; idx++) {
            int[] com = commands[idx];
            int start = com[0] - 1;
            int end = com[1] - 1;
            int k = com[2];
            
            // 1. i에서 j까지 자르기
            int[] sub_arr = new int[end - start + 1];
            
            for (int i = start; i < end+1; i++) {
                sub_arr[i-start] = array[i];
            }
            
            // 2. 1에서 나온 배열을 정렬하기
            Arrays.sort(sub_arr);
            
            // 3. 2에서 나온 배열의 k번쟤 숫자
            int result = sub_arr[k-1];
            
            // answer에 담기
            answer[idx] = result;
        }
        
        
        return answer;
    }
}