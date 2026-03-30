import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] score;
	static int[][] game;
	static boolean possible;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		game = new int[15][2];
		int idx = 0;
		for (int i = 0; i < 6; i++) {
			for (int j = i + 1; j < 6; j++) {
				game[idx][0] = i;
				game[idx][1] = j;
				idx += 1;
			}
		}
		
		
		for (int i = 0; i < 4; i++) {
			score = new int[6][3];
			
			int wSum = 0;
			int dSum = 0;
			int fSum = 0;
			
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 6; j++) {
				int w = Integer.parseInt(st.nextToken());
				int d = Integer.parseInt(st.nextToken());
				int f = Integer.parseInt(st.nextToken());
				
				wSum += w;
				dSum += d;
				fSum += f;
				
				score[j][0] = w;
				score[j][1] = d;
				score[j][2] = f;
			}
			
			// 1. 승의 합 = 패의 합인지
			if (wSum != fSum) {
				System.out.print(0 + " ");
				continue;
			}
			
			// 2. 승, 무, 패의 합이 30인지
			if (wSum + dSum + fSum != 30) {
				System.out.print(0 + " ");
				continue;
			}
			
			// 3. 무의 합이 짝수인지
			if (dSum % 2 != 0) {
				System.out.print(0 + " ");
				continue;
			}
			
			// 4. DFS로 확인
			possible = false;
			DFS(0);
			
			if (possible) {
				System.out.print(1 + " ");
			} else {
				System.out.print(0 + " ");
			}
		}
	}
	
	static void DFS(int idx) {
		if (possible) {
			return;
		}
		
		if (idx == 15) {
			possible = true;
			return;
		}
		
		int a = game[idx][0];
		int b = game[idx][1];
		
		// 1. a승 b패
		if (score[a][0] > 0 && score[b][2] > 0) {
			score[a][0] -= 1;
			score[b][2] -= 1;
			
			DFS(idx + 1);
			
			score[a][0] += 1;
			score[b][2] += 1;
		}
		
		// 2. a무 b무
		if (score[a][1] > 0 && score[b][1] > 0) {
			score[a][1] -= 1;
			score[b][1] -= 1;
			
			DFS(idx + 1);
			
			score[a][1] += 1;
			score[b][1] += 1;
		}
		
		// 3. a패 b승
		if (score[a][2] > 0 && score[b][0] > 0) {
			score[a][2] -= 1;
			score[b][0] -= 1;
			
			DFS(idx + 1);
			
			score[a][2] += 1;
			score[b][0] += 1;
		}
		
		
	}
}
