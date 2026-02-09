import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		
		boolean[][] ground = new boolean[100][100];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int firstC = Integer.parseInt(st.nextToken());
			int firstR = Integer.parseInt(st.nextToken());
			
			for (int c = firstC; c < firstC + 10; c++) {
				for (int r = firstR; r < firstR + 10; r++) {
					ground[r][c] = true;
				}
			}
		}
		
		int result = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (ground[i][j] == true) {
					result += 1;
				}
			}
		}
		
		System.out.println(result);
	}
}
