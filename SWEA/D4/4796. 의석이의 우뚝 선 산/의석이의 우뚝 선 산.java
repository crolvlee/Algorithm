import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			// 1. 입력받기
			int N = sc.nextInt();
            int[] hArr = new int[N];

            for (int i = 0; i < N; i++) {
                hArr[i] = sc.nextInt();
            }
			
			// 2. 각 점의 왼쪽, 오른쪽의 방향 확인
			// 1: 상상 / 2: 상하(극대) / 3: 하하 / 4: 하상(극소)
			int[] arr = new int[N];
			
			// 양끝 두개는 임의로 4로 두기
			arr[0] = 4;
			arr[N-1] = 4;
			
			for (int i = 1; i <= N-2; i++) {
				int prevH = hArr[i-1];
				int nowH = hArr[i];
				int nextH = hArr[i+1];
				
				if (prevH < nowH && nowH < nextH) { // 1. 상상
					arr[i] = 1;
				} else if (prevH < nowH && nowH > nextH) { // 2. 상하
					arr[i] = 2;
				} else if (prevH > nowH && nowH > nextH) { // 3. 하하
					arr[i] = 3;
				} else { // 4. 하상
					arr[i] = 4;
				}
			}
			
			// 3. 4___2___4 인 그룹 찾기 (왼쪽은 up / 오른쪽은 down)
			int answer = 0;
			
			int upCnt = 0;
			int downCnt = 0;
			boolean exist2 = false;
			for (int i = 0; i < N; i++) {
				if (arr[i] == 1) {
					upCnt += 1;
				} else if (arr[i] == 2) {
					exist2 = true;
				} else if (arr[i] == 3) {
					downCnt += 1;
				} else if (arr[i] == 4) {
					if (exist2 == true) {
						answer += (upCnt + 1) * (downCnt + 1);
					}
					upCnt = 0;
					downCnt = 0;
					exist2 = false;
				}
			}
			
			System.out.println("#" + tc + " " + answer);
		}
	}
}
