import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int[] dr = {0, 0, 1, -1}; // 동서남북
	static int[] dc = {1, -1, 0, 0};
	static int N;
	static int[][] ground;
	static int resultNode;
	static int resultCount;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			ground = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				
				for (int j = 0; j < N; j++) {
					ground[i][j] = Integer.parseInt(st.nextToken()); 
				}
			}
			
			resultNode = 2000;
			resultCount = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					DFS(i, j, 1, ground[i][j]);
				}
			}
			
			System.out.println("#" + tc + " " + resultNode + " " + resultCount);
		}
	}
	
	static void DFS(int nowRow, int nowCol, int count, int startNum) {
		for (int i = 0; i < 4; i++) {
			int nextRow = nowRow + dr[i];
			int nextCol = nowCol + dc[i];
			
			if (0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < N) {
				if (ground[nextRow][nextCol] == ground[nowRow][nowCol] + 1) {
					DFS(nextRow, nextCol, count + 1, startNum);
				}
			}
		}
		
		if (count > resultCount) {
			resultCount = count;
			resultNode = startNum;
		} else if (count == resultCount) {
			resultNode = Math.min(startNum, resultNode);
		}
	}
}
