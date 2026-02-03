import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] nums = new int[N+1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < N+1; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] dp = new int[N+1];
		dp[0] = 0;
		for (int i = 1; i < N+1; i++) {
			dp[i] = dp[i-1] + nums[i];
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			System.out.println(dp[end] - dp[start-1]);
		}
	}
}