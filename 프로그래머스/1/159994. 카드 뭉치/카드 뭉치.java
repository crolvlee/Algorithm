class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        
        int first_idx = 0;
        int second_idx = 0;
        
        for (String word : goal) {
            
            if (first_idx < cards1.length && cards1[first_idx].equals(word)) {
                // 1. 목표 word가 first_idx에 있는 경우
                first_idx += 1;
                
            } else if (second_idx < cards2.length && cards2[second_idx].equals(word)) {
                // 2. 목표 word가 second_idx에 있는 경우
                second_idx += 1;
                
            } else {
                // 3. 목표 word가 없는 경우
                answer = "No";
                break;
            }
            
        }
        
        return answer;
    }
}