import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		// 1. 초기 입력받기
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		int[][] ground = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				ground[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 2. 위치 옮기기
		int groupCnt = Math.min(N, M) / 2;
		
		for (int i = 0; i < groupCnt; i++) {
			// 2-1. 현재 그룹 내부의 원소 리스트 만들기
			int nowGroupCnt = 2*M + 2*N - 8*i - 4;
			int[] nowGroupArr = new int[nowGroupCnt];
			
			int idx = 0;
			
			// i행 전부
			for (int a = i; a < M-i; a++) {
				nowGroupArr[idx] = ground[i][a];
				idx += 1;
			}
			
			// (M-1-i)열 (양끝 2개 빼고)
			for (int a = i+1; a < N-1-i; a++) {
				nowGroupArr[idx] = ground[a][M-1-i];
				idx += 1;
			}
			
			// (N-1-i)행
			for (int a = M-1-i; a >= i; a--) {
				nowGroupArr[idx] = ground[N-1-i][a];
				idx += 1;
			}
			
			// i열 (양끝 2개 빼고)
			for (int a = N-2-i; a > i; a--) {
				nowGroupArr[idx] = ground[a][i];
				idx += 1;
			}
			
			// 2-2. 현재 그룹 내부의 원소 위치 옮기기
			int rotateCnt = R % nowGroupCnt;
			int nIdx = 0;
			
			// i행 전부
			for (int a = i; a < M-i; a++) {
				ground[i][a] = nowGroupArr[(rotateCnt + nIdx) % nowGroupCnt];
				nIdx += 1;
			}
			
			// (M-1-i)열 (양끝 2개 빼고)
			for (int a = i+1; a < N-1-i; a++) {
				ground[a][M-1-i] = nowGroupArr[(rotateCnt + nIdx) % nowGroupCnt];
				nIdx += 1;
			}
			
			// (N-1-i)행
			for (int a = M-1-i; a >= i; a--) {
				ground[N-1-i][a] = nowGroupArr[(rotateCnt + nIdx) % nowGroupCnt];
				nIdx += 1;
			}
			
			// i열 (양끝 2개 빼고)
			for (int a = N-2-i; a > i; a--) {
				ground[a][i] = nowGroupArr[(rotateCnt + nIdx) % nowGroupCnt];
				nIdx += 1;
			}
		}
		
		// 3. 출력
		for (int[] line : ground) {
			for (int i = 0; i < line.length; i++) {
				System.out.print(line[i]);
				if (i < line.length - 1) {
					System.out.print(" ");
				}
			}
			System.out.println();
		}
	}
}
