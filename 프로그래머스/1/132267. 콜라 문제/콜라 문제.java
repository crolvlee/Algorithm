// a개를 주면 -> b개를 받음

// a = 10, b = 3
// 10개 보유 -> 10개 줌 -> 3개를 받음
// 19개 보유 -> 10개 줌 -> 3개를 받음
// n개 보유  -> (n / a) * a개 줌 -> (n / a) * b개 받음

// 보유 중인 빈 병이 2개 미만이면 -> 콜라를 받을 수 없음

class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;     // 받는 콜라의 개수
        int sang_cola = n;  // 보유한 콜라 개수
        
        while (true) {
            if (sang_cola < a) {
                break;
            }
            
            int give_cola = (sang_cola / a) * a;
            int new_cola = (sang_cola / a) * b;
            answer += new_cola;
            sang_cola = sang_cola - give_cola + new_cola;
            
            // System.out.println(new_cola);
            // System.out.println(sang_cola);
            // System.out.println("----");
        }
        
        return answer;
    }
}