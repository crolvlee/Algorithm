import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution {
	
	static int[] nums; // 0: 인영, 1: 규영
	static int[] kyuNums;
	static int[] inNums;
	static boolean[] visited; // 인영 카드
	static int[] inPermutationPath;
	static int kyuWinCnt;
	static int kyuLoseCnt;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			nums = new int[19];
			kyuNums = new int[9];
			inNums = new int[9];
			visited = new boolean[9];
			inPermutationPath = new int[9];
			kyuWinCnt = 0;
			kyuLoseCnt = 0;
			
			st = new StringTokenizer(br.readLine());
			
			for (int i = 0; i < 9; i++) {
				int now_num = Integer.parseInt(st.nextToken());
				kyuNums[i] = now_num;
				nums[now_num] = 1;
			}
			
			int idx = 0;
			for (int i = 1; i <= 18; i++) {
				if (nums[i] == 0) {
					inNums[idx] = i;
					idx += 1;
				}
			}
			
			// 순열로 탐색
			permutation(0);
			System.out.println("#" + tc + " " + kyuWinCnt + " " + kyuLoseCnt);
		}
	}
	
	static void permutation(int depth) {
		if (depth == 9) {
			if (isKyuWin()) {
				kyuWinCnt += 1;
			} else {
				kyuLoseCnt += 1;
			}
			
			return;
		}
		
		for (int i = 0; i < 9; i++) {
			if (visited[i] == false) {
				inPermutationPath[depth] = inNums[i];
				visited[i] = true;
				permutation(depth + 1);
				inPermutationPath[depth] = 0;
				visited[i] = false;
			}
		}
	}
	
	static boolean isKyuWin() {
		int kyuTotal = 0;
		int inTotal = 0;
		
		for (int i = 0; i < 9; i++) {
			int kyuNum = kyuNums[i];
			int inNum = inPermutationPath[i];
			
			if (kyuNum < inNum) {
				inTotal += (kyuNum + inNum);
			} else {
				kyuTotal += (kyuNum + inNum);
			}
		}
		
		if (kyuTotal > inTotal) {
			return true;
		} else {
			return false;
		}
	}
}
