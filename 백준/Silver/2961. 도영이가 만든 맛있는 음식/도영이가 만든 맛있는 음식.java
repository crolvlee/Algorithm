import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int answer = 999999999;
	static int[][] flavors;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		flavors = new int[N][2];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int S = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			
			flavors[i][0] = S;
			flavors[i][1] = B;
		}
		
		DFS(0, 1, 0, 0);
		System.out.println(answer);
	}
	
	private static void DFS(int depth, int totalS, int totalB, int cnt) {
		if (depth == N) {
			if (cnt > 0) {
				int result = Math.abs(totalS - totalB);
				answer = Math.min(answer, result);
				return;
			}
			return;
		}

		DFS(depth + 1, totalS * flavors[depth][0], totalB + flavors[depth][1], cnt + 1);
		DFS(depth + 1, totalS, totalB, cnt);
	}
}
