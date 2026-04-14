import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int INF = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws Exception {
		// System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());
			
			int[][] distance = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (i == j) {
						distance[i][j] = 0;
					} else {
						distance[i][j] = INF;
					}
				}
			}
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				distance[a-1][b-1] = 1;
			}
			
			// 플로이드
			for (int k = 0; k < N; k++) {
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						if (distance[i][k] != INF && distance[k][j] != INF) {
							if (distance[i][k] + distance[k][j] < distance[i][j]) {
								distance[i][j] = distance[i][k] + distance[k][j];
							}
						}
					}
				}
			}
			
			int answer = 0;
			
			for (int i = 0; i < N; i++) {
				// 특정점이 이동할 수 있는 다른 점의 개수 x
				int x = 0;
				for (int j = 0; j < N; j++) {
					if (distance[i][j] != 0 && distance[i][j] != INF) {
						x += 1;
					}
				}
				
				// 특정점으로 이동올 수 있는 다른 점의 개수 y
				int y = 0;
				for (int j = 0; j < N; j++) {
					if (distance[j][i] != 0 && distance[j][i] != INF) {
						y += 1;
					}
				}
				
				if (x + y == N-1) {
					answer += 1;
				}
			}
			
			System.out.println("#" + tc + " " + answer);
		}
		
	}
}
