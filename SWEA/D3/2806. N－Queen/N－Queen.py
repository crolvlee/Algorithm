import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static boolean[] colSelected;
	static int[] colNums;
	static int answer;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			colSelected = new boolean[N];
			colNums = new int[N];
			answer = 0;
			
			backtracking(0);
			
			System.out.println("#" + tc + " " + answer);
		}
	}
	
	static void backtracking(int nowRow) {
		if (nowRow == N) {
			answer += 1;
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (!colSelected[i] && !diagonal(nowRow, i)) {
				colSelected[i] = true;
				colNums[nowRow] = i;
				backtracking(nowRow + 1);
				colSelected[i] = false;
				colNums[nowRow] = 0;
			}
		}
	}
	
	static boolean diagonal(int nowRow, int nowCol) {
		for (int prevRow = 0; prevRow < nowRow; prevRow++) {
			int prevCol = colNums[prevRow];
			
			// (1) 방향이 /인 대각선
			// (2) 방향이 \인 대각선
			if ((prevRow - nowRow == prevCol - nowCol) || (prevRow - nowRow == - prevCol + nowCol)) {
				return true;
			}
		}
		return false;
	}
}
