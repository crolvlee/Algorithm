import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
	static class Node {
		int row, col, dir, power;
		Node (int row, int col, int dir, int power) {
			this.row = row;
			this.col = col;
			this.dir = dir;
			this.power = power;
		}
	}
	
	static int[] dr = {-1, 1, 0, 0}; // 상, 하, 좌, 우
	static int[] dc = {0, 0, -1, 1};
	static int N;
	static int[][] ground = new int[4001][4001];
	static Queue<Node> q;
	static int result;
	
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
			q = new LinkedList<>();

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				int dir = Integer.parseInt(st.nextToken());
				int power = Integer.parseInt(st.nextToken());

				int row = (1000 - y) * 2;
				int col = (1000 + x) * 2;
				
				ground[row][col] = power;
				q.add(new Node(row, col, dir, power));
			}
			
			result = 0;
			bfs();
			System.out.println("#" + tc + " " + result);
		}
	}
	
	static void bfs() {
		while (!q.isEmpty()) {
			Node nowNode = q.poll();
			
			// 현재 칸이 다른 원자들과 합쳐진 상태라면
			if (ground[nowNode.row][nowNode.col] != nowNode.power) {
				result += ground[nowNode.row][nowNode.col];
				ground[nowNode.row][nowNode.col] = 0;
				continue;
			}
			
			int nextRow = nowNode.row + dr[nowNode.dir];
			int nextCol = nowNode.col + dc[nowNode.dir];
			
			if (0 <= nextRow && nextRow <= 4000 && 0 <= nextCol && nextCol <= 4000) {
				if (ground[nextRow][nextCol] == 0) { // nextNode가 비어있는 경우
					ground[nextRow][nextCol] = nowNode.power;
					q.add(new Node(nextRow, nextCol, nowNode.dir, nowNode.power));
				} else { // nextNode에 이미 다른 원자가 있는 경우
					ground[nextRow][nextCol] += nowNode.power;
				}
			}
			
			ground[nowNode.row][nowNode.col] = 0;
		}
	}
}
