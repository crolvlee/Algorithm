import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= T; tc++) {
            // 1. 입력받기
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] arr = new int[N];
            int maxH = 0;

            for (int i = 0; i < N; i++) {
                int now_num = Integer.parseInt(st.nextToken());
                arr[i] = now_num;
                maxH = Math.max(maxH, now_num);
            }

            // 2. 필요한 (+1)의 개수, (+2)의 개수
            int odd = 0;
            int even = 0;

            for (int i = 0; i < N; i++) {
                int d = maxH - arr[i];
                odd += (d % 2);
                even += (d / 2);
            }

            // 3. 균형 맞추기 (even이 월등히 클 때가 문제. 쪼개줄 수 있음 / odd가 월등히 클 때는 처리해줄 수 있는 게 없음)
            while (even > odd  + 1) {
                even -= 1;
                odd += 2;
            }

            // 4. 최종 날짜 수 구하기
            int result = 0;
            if (odd > even)  {
                result = (odd * 2) - 1;
            } else if (odd == even) {
                result = odd * 2;
            } else if (odd < even) {
                result = even * 2;
            }

            System.out.println("#" + tc + " " + result);
        }
    }
}