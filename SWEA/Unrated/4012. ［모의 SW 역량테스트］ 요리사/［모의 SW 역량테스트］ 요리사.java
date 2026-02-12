import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static int[][] table;
	static int[] group; // 1: 그룹A에 들어가는 식재료 / 0: 그룹B에 들어가는 식재료
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
			table = new int[N][N];
			group = new int[N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				
				for (int j = 0; j < N; j++) {
					table[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 2. 식재료를 두 그룹으로 만들어서 계산하기
			group[0] = 1; // 0번 식재료는 항상 그룹A에 들어감
			result = 2000000;
			makeCombi(1, 1);
			
			System.out.println("#" + tc + " " + result);
		}
	}
	
	static void makeCombi(int start, int count) {
		if (count == N / 2) {
			int flavorDiff = calcDiff();
			result = Math.min(result, flavorDiff);
			return;
		}
		
		for (int i = start; i < N; i++) {
			group[i] = 1;
			makeCombi(i + 1, count+1);
			group[i] = 0;
		}
	}
	
	static int calcDiff() {
		List<Integer> groupA = new ArrayList<>();
		List<Integer> groupB = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			if (group[i] == 1) {
				groupA.add(i);
			} else if (group[i] == 0) {
				groupB.add(i);
			}
		}
		
		// A의 맛
		int aS = 0;
		for (int i = 0; i < N/2; i++) {
			for (int j = 0; j < N/2; j++) {
				if (i != j) {
					aS += table[groupA.get(i)][groupA.get(j)];
				}
			}
		}
		
		// B의 맛
		int bS = 0;
		for (int i = 0; i < N/2; i++) {
			for (int j = 0; j < N/2; j++) {
				if (i != j) {
					bS += table[groupB.get(i)][groupB.get(j)];
				}
			}
		}
		
		return Math.abs(aS - bS);
	}
}
