// 접두어 관계 O -> false 리턴
// 접두어 관계 X -> true 리턴

import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        // map에 단어 넣기
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < phone_book.length; i++) {
            map.put(phone_book[i], i);
        }
        
        // 단어 순회하기 -> 단어의 접두어가 map에 있는 경우 answer를 false 처리
        for (int i = 0; i < phone_book.length; i++) {
            String now_word = phone_book[i];
            
            for (int j = 0; j < now_word.length(); j++) {
                String now_front = now_word.substring(0, j);
                if (map.containsKey(now_front)) {
                    answer = false;
                    break;
                }
            }
        }
        
        
        
        return answer;
    }
}