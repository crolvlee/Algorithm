import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            long N = Long.parseLong(st.nextToken());

            long count = 0;
            long nowNum = N;

            while (nowNum != 2) {
                long sqrtNum = (long) Math.sqrt(nowNum);
                if (sqrtNum * sqrtNum == nowNum) {      // 1. 제곱수인 경우
                    count += 1;
                    nowNum = sqrtNum;
                } else {                                // 2. 제곱수가 아닌 경우
                    count += ((sqrtNum + 1) * (sqrtNum + 1) - nowNum);
                    nowNum = (sqrtNum + 1) * (sqrtNum + 1);
                }
            }

            System.out.println("#" + tc + " " + count);

        }
    }
}