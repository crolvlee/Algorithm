import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int N, M, C;
	static int[][] ground;
	static int[] combinationPath;
	static int result;
	static int totalProfit;
	static boolean[] mask;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			// 1. 입력받기
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken()); // 벌통 크기
			M = Integer.parseInt(st.nextToken()); // 선택할 수 있는 벌통의 개수
			C = Integer.parseInt(st.nextToken()); // 꿀을 채취할 수 있는 최대 양
			
			ground = new int[N][N];
			combinationPath = new int[2];
			result = 0;
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					ground[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 2. (0, 0) ~ (N-1, N-2) 까지의 벌통 중 2개를 선택
			// 단, (c1 - c2)의 절댓값은 1이면 안됨
			combination(0, 0);
			System.out.println("#" + tc + " " + result);
		}
	}
	
	static void combination(int start, int depth) {
		if (depth == 2) {
			int numA = combinationPath[0];
			int numB = combinationPath[1];
			if (Math.abs(numA-numB) <= M - 1) {
				return;
			}
			
			// 숫자를 r, c로 변환하기
			int rowA = numA / N;
			int colA = numA % N;
			int rowB = numB / N;
			int colB = numB % N;
			
			// 채취할 수 있는 꿀의 양 구하기
			int honeyA = calculate(rowA, colA);
			int honeyB = calculate(rowB, colB);
			
			result = Math.max(result, honeyA + honeyB);
			return;
		}
		
		for (int i = start; i < N*N; i++) {
			if (i % N < N - M + 1) {
				combinationPath[depth] = i;
				combination(i + 1, depth + 1);
				combinationPath[depth] = 0;
			}
		}
	}
	
	static int calculate(int nowRow, int firstCol) {
		totalProfit = 0;
		mask = new boolean[M] ;
		DFS(nowRow, firstCol, 0, 0);
		
		return totalProfit;
	}
	
	static void DFS(int nowRow, int nowCol, int depth, int total) {
		if (depth == M) {
			if (total <= C) {
				int nowProfit = 0;
				int startCol = nowCol - M;
				for (int i = 0; i < M; i++) {
					if (mask[i]) {
						int num = ground[nowRow][startCol + i];
						nowProfit += num * num;
					}
				}
				
				totalProfit = Math.max(totalProfit, nowProfit);
			}
			return;
		}
		
		mask[depth] = true;
		DFS(nowRow, nowCol + 1, depth + 1, total + ground[nowRow][nowCol]);
		mask[depth] = false;
		DFS(nowRow, nowCol + 1, depth + 1, total);
		
		return;
	}
}
