import java.util.*;

class Solution {
    public int[] solution(String s) {
        
        // result 리스트
        List<Integer> result = new ArrayList<>();
        
        // 이전에 나온 것을 map에 넣기
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char now_ch = s.charAt(i);
            String now_str = String.valueOf(now_ch);
            
            if (map.containsKey(now_str) == true) {
                // 이전에 나온적이 있다면
                int last_idx = map.get(now_str);
                result.add(i - last_idx);
                map.put(now_str, i);
            } else {
                // 이전에 나온적이 없다면
                result.add(-1);
                map.put(now_str, i);
            }
        }
        
        // result 리스트 -> answer 배열
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}