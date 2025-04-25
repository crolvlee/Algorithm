import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        
        List<String> list = new ArrayList<>();
        
        for (int i = 0; i < strings.length; i++) {
            String word = strings[i];
            String n_str = word.substring(n, n+1); // n번째 숫잦
            
            String new_word = n_str + word;
            list.add(new_word);
        }
        
        Collections.sort(list);
        
        
        // list 리스트 -> answer 배열
        String[] answer = new String[list.size()];
        
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i).substring(1);
        }
        
        return answer;
    }
}