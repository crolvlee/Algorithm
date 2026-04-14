import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		// System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken()); // 물건의 개수
			int K = Integer.parseInt(st.nextToken()); // 가방의 부피
			
			int[][] table = new int[N+1][K+1];

			for (int i = 1; i < N+1; i++) {
				st = new StringTokenizer(br.readLine());
				int V = Integer.parseInt(st.nextToken()); // 물건의 부피
				int C = Integer.parseInt(st.nextToken()); // 물건의 가치
				
				for (int j = 1; j < K+1; j++) {
					if (j < V) {
						table[i][j] = table[i-1][j];
					} else {
						table[i][j] = Math.max(table[i-1][j], table[i-1][j-V] + C);
					}
				}
			}
			
			int answer = table[N][K];
			
			System.out.println("#" + tc + " " + answer);
		}
	}
}
