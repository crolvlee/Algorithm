import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int midIdx = N / 2;
			int answer = 0;
			
			for (int i = 0; i < N; i++) {
				String line = br.readLine();
				
				for (int j = 0; j < N; j++) {
					int nowNum = line.charAt(j) - '0';
					
					if (i <= midIdx) { // 위쪽인 경우
						if (midIdx - i <= j && j <= midIdx + i) {
							answer += nowNum;
						}
					} else { // 아랫쪽인 경우
						if (i - midIdx <= j && j <= -i + midIdx + N - 1) {
							answer += nowNum;
						}
					}
				}
			}
			
			System.out.println("#" + tc + " " + answer);
		}
	}
}
