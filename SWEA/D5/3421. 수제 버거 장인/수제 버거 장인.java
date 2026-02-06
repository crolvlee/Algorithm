import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Solution {
	static int N, M;
	static boolean[] subsetMask;
	static int[][] notMatchIdxs;
	static int answer;
	
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
			M = Integer.parseInt(st.nextToken());
			subsetMask = new boolean[N+1];
			notMatchIdxs = new int[M][2];
			answer = 0;
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				notMatchIdxs[i][0] = a;
				notMatchIdxs[i][1] = b;
			}
			
			// 2. 부분집합 만들기
			DFS(1);
			System.out.println("#" + tc + " " + answer);
		}
		
	}
	
	private static void DFS(int depth) {
		if (depth == N + 1) {
			boolean canMake = true;
			
			for (int[] notMatch : notMatchIdxs) {
				int idxA = notMatch[0];
				int idxB = notMatch[1];
				
				if (subsetMask[idxA] && subsetMask[idxB]) {
					canMake = false;
					break;
				}
			}
			
			if (canMake == true) {
				answer += 1;
			}
			
			return;
		}
		
		subsetMask[depth] = true;
		DFS(depth + 1);
		subsetMask[depth] = false;
		DFS(depth + 1);
	}
}
