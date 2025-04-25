import java.util.*;

class Solution {
    boolean solution(String s) {
        
        List<String> list = new ArrayList<String>();

        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            if (now == '(') {
                String now_str = String.valueOf(now);
                list.add(now_str);
            } else if (now == ')') {
                if (list.size() > 0 && list.get(list.size() - 1).equals("(")) {
                    list.remove(list.size() - 1);
                } else {
                    String now_str = String.valueOf(now);
                    list.add(now_str);
                }
            }
        }
        
        System.out.println(list);
        
        // answer 담기
        boolean answer = true;
        if (list.size() > 0) {
            answer = false;
        }

        return answer;
    }
}