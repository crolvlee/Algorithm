class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        
        // p의 길이
        int p_len = p.length();
        
        // p의 long형
        long p_long = Long.parseLong(p);
        
        // t에서 길이가 p_len인 문자열 찾기
        for (int i = 0; i < t.length() - p_len + 1; i++) {
            String now_str = "";
            
            for (int j = 0; j < p_len; j++) {
                now_str += t.charAt(i + j);
            }
            
            // String -> long
            long now_long = Long.parseLong(now_str);
            
            if (now_long <= p_long) {
                answer += 1;
            }
            
        }
        
        
        return answer;
    }
}