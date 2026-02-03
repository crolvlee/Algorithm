import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		// 1. 기본 배열 입력받기
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] ground = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				ground[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 2. 합 dp 배열 만들기
		int[][] dp = new int[N+1][N+1];
		
		// 1행 채우기
		dp[1][1] = ground[0][0];
		for (int i = 2; i <= N; i++) {
			dp[1][i] = dp[1][i-1] + ground[0][i-1];
		}
		
		// 1열 채우기
		for (int i = 2; i <= N; i++) {
			dp[i][1] = dp[i-1][1] + ground[i-1][0];
		}
		
		// 나머지 채우기
		for (int i = 2; i <= N; i++) {
			for (int j = 2; j <= N; j ++) {
				dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + ground[i-1][j-1];
			}
		}
		
		// 3. 구간 합 찾기		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			int result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 -1][y1 - 1];
			System.out.println(result);
		}
	}
}