import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution { 
	static int N, X, M;
	static int[] result;
	static int[] answer;
	static int[][] records;
	static int maxSum;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			// 1. 입력받기
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			X = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			records = new int[M][3];
			result = new int[N];
			answer = new int[N];
			maxSum = -1;
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int l = Integer.parseInt(st.nextToken()) - 1;
				int r = Integer.parseInt(st.nextToken()) - 1;
				int s = Integer.parseInt(st.nextToken());
				
				records[i][0] = l;
				records[i][1] = r;
				records[i][2] = s;
			}
			
			DFS(0);
			
			System.out.print("#" + tc + " ");
			if (maxSum == -1) {
				System.out.println(-1);
			} else {
				for (int num : answer) {
					System.out.print(num + " ");
				}
				System.out.println();
			}
		}
	}
	
	static void DFS(int depth) {
		if (depth == N) {
			// records 돌면서 조건 만족하는지 확인
			for (int i = 0; i < M; i++) {
				int checkSum = 0;
				for (int j = records[i][0]; j <= records[i][1]; j++) {
					checkSum += result[j];
				}
				
				if (checkSum != records[i][2]) {
					return;
				}
			}
			
			// 조건 다 만족하는 경우, 전역에 있는 maxSum과 비교
			int sum = 0;
			for (int num : result) {
				sum += num;
			}
			
			if (sum > maxSum) {
				maxSum = sum;
				answer = Arrays.copyOf(result, N);
			}
			
			return;
		}
		
		for (int i = 0; i <= X; i++) {
			result[depth] = i;
			DFS(depth + 1);
		}
	}
}
