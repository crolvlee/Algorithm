import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        
        // numbers 배열에서 두 수를 골라 result 리스트에 담기
        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int now_sum = numbers[i] + numbers[j];
                if (result.contains(now_sum) == false) {
                    result.add(now_sum);
                }
            }
        }
        
        Collections.sort(result);
        
        System.out.println(result);
        
        // result 리스트 -> answer 배열
        int[] answer = new int[result.size()];
        
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        
        return answer;
    }
}