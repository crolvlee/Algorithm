// 제일 왼쪽 위를 0행 0열로 설정

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static int[] dr = {0, -1, 0, 1, 0}; // 상우하좌
	static int[] dc = {0, 0, 1, 0, -1};
	static int M;
	static int A;
	static int[] arrA; // A의 이동방향
	static int[] arrB; // B의 이동방향
	static int[][] groundBC; // 각 위치에 있는 충전기들 (1, 2, 3,...)
	static int[] arrBCP;
	static boolean[][] visited;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {

			// 1. 입력받기
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			A = Integer.parseInt(st.nextToken());
			arrA = new int[M + 1];
			arrB = new int[M + 1];
			groundBC = new int[10][10];
			arrBCP = new int[A];
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				arrA[i] = Integer.parseInt(st.nextToken());
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				arrB[i] = Integer.parseInt(st.nextToken());
			}
			
			for (int i = 0; i < A; i++) {
				st = new StringTokenizer(br.readLine()); // [행번호, 열번호, 충전범위, 성능]
				int col = Integer.parseInt(st.nextToken()) - 1;
				int row = Integer.parseInt(st.nextToken()) - 1;
				int c = Integer.parseInt(st.nextToken());
				int p = Integer.parseInt(st.nextToken());
				
				fillGroundBC(row, col, i, c);
				arrBCP[i] = p;
			}
			
			// 2. 시간에 따라 A, B의 위치 이동
			int aRow = 0;
			int aCol = 0;
			int bRow = 9;
			int bCol = 9;
			int total = 0;
			
			for (int i = 0; i <= M; i++) {
				// A. B의 현재 위치에서 충전 가능한 충전기
				List<Integer> aBCList = new ArrayList<>();
				List<Integer> bBCList = new ArrayList<>();
				int aMask = groundBC[aRow][aCol];
				int bMask = groundBC[bRow][bCol];
				
				for (int bcNum = 0; bcNum < A; bcNum++) {
					if ((aMask & (1 << bcNum)) != 0) {
						aBCList.add(bcNum);
					}
				}
				
				for (int bcNum = 0; bcNum < A; bcNum++) {
					if ((bMask & (1 << bcNum)) != 0) {
						bBCList.add(bcNum);
					}
				}
				
				// 가능한 충전기 찾기
				if (aBCList.size() > 0 && bBCList.size() == 0) { // A만 충전 가능한 경우
					int maxP = 0;
					for (int ai = 0; ai < aBCList.size(); ai++) {
						int aP = arrBCP[aBCList.get(ai)];
						maxP = Math.max(aP, maxP);
					}
					total += maxP;
				} else if (aBCList.size() == 0 && bBCList.size() > 0) { // B만 충전 가능한 경우
					int maxP = 0;
					for (int bi = 0; bi < bBCList.size(); bi++) {
						int bP = arrBCP[bBCList.get(bi)];
						maxP = Math.max(bP, maxP);
					}
					total += maxP;
				} else if (aBCList.size() == 0 && bBCList.size() == 0) { // 둘 다 충전 불가능한 경우
					
				} else if (aBCList.size() > 0 && bBCList.size() > 0) { // 둘 다 충전 가능한 경우
					int numsAdd = bcBoth(aBCList, bBCList);
					total += numsAdd;
				}
				
				// A와 B의 위치 옮기기
				aRow += dr[arrA[i]];
				aCol += dc[arrA[i]];
				bRow += dr[arrB[i]];
				bCol += dc[arrB[i]];
			}
			
			System.out.println("#" + tc  + " " + total);
		}
	}
	
	// 현재 위치에서 A, B가 선택할 충전기를 찾는 함수
	static int bcBoth(List<Integer> aBCList, List<Integer> bBCList) {
	    int best = 0;

	    for (int i = 0; i < aBCList.size(); i++) {
	        int aBC = aBCList.get(i);
	        int aP = arrBCP[aBC];

	        for (int j = 0; j < bBCList.size(); j++) {
	            int bBC = bBCList.get(j);
	            int bP = arrBCP[bBC];

	            int sum;
	            if (aBC == bBC) { // 같은 BC를 공유하는 경우
	                sum = aP;
	            } else {
	                sum = aP + bP;
	            }

	            best = Math.max(best, sum);
	        }
	    }

	    return best;
	}

	
	// groundBC에 영역 표시하는 함수
	static void fillGroundBC(int startRow, int startCol, int numBC, int c) {
		Queue<int[]> q = new LinkedList<>();
		visited = new boolean[10][10];
		q.add(new int[] {startRow, startCol, 0});
		groundBC[startRow][startCol] |= (1 << numBC);
		visited[startRow][startCol] = true;
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			int nowRow = now[0];
			int nowCol = now[1];
			int nowDepth = now[2];
			
			if (nowDepth == c) {
				continue;
			}
			
			for (int i = 1; i <= 4; i++) {
				int nextRow = nowRow + dr[i];
				int nextCol = nowCol + dc[i];
				
				if (0 <= nextRow && nextRow <= 9 && 0 <= nextCol && nextCol <= 9 && !visited[nextRow][nextCol]) {
					q.add(new int[] {nextRow, nextCol, nowDepth + 1});
					groundBC[nextRow][nextCol] |= (1 << numBC);
					visited[nextRow][nextCol] = true;
				}
			}
		}
	}
}
