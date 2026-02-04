import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int[][] ground;
	static int answer;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		for (int tc = 1; tc <= 10; tc++) {
			st = new StringTokenizer(br.readLine());
			String _ = st.nextToken();
			ground = new int[100][100];
			
			int endCol = 0;
			
			for (int i = 0; i < 100; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 100; j++) {
					int num = Integer.parseInt(st.nextToken());
					if (num == 2) {
						endCol = j;
					}
					ground[i][j] = num;
				}
			}
			
			DFS(99, endCol, 'B');
			System.out.println("#" + tc + " " + answer);
		}
	}
	
	private static void DFS(int nowRow, int nowCol, char direction) {
		if (nowRow == 0) {
			answer = nowCol;
			return;
		}
		
		if (direction == 'B') { // 1. 아래에서 온 경우
			if (0 <= nowCol - 1 && nowCol - 1 <= 99 && ground[nowRow][nowCol - 1] == 1) {
				DFS(nowRow, nowCol - 1, 'R');
			} else if (0 <= nowCol + 1 && nowCol + 1 <= 99 && ground[nowRow][nowCol + 1] == 1) {
				DFS(nowRow, nowCol + 1, 'L');
			} else {
				DFS(nowRow - 1, nowCol, 'B');
			}
		} else if (direction == 'L') { // 2. 왼쪽에서 온 경우
			if (ground[nowRow - 1][nowCol] == 1) {
				DFS(nowRow - 1, nowCol, 'B');
			} else if (0 <= nowCol + 1 && nowCol + 1 <= 99 && ground[nowRow][nowCol + 1] == 1) {
				DFS(nowRow, nowCol + 1, 'L');
			}
		} else if (direction == 'R') { // 3. 오른쪽에서 온 경우
			if (ground[nowRow - 1][nowCol] == 1) {
				DFS(nowRow - 1, nowCol, 'B');
			} else if (0 <= nowCol - 1 && nowCol - 1 <= 99 && ground[nowRow][nowCol - 1] == 1) {
				DFS(nowRow, nowCol - 1, 'R');
			}
		}
	}
}
