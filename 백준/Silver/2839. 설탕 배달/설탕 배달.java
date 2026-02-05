import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		boolean find = false;
		int result = 1666;
		
		for (int i = (N/5); i >= 0; i--) {
			int bongCnt = i;
			
			int fiveTotal = i * 5;
			int threeTotal = N - fiveTotal;
			
			if (threeTotal % 3 == 0) {
				bongCnt += (threeTotal / 3);
				find = true;
				result = Math.min(result, bongCnt);
			} else {
				continue;
			}
		}
		
		if (find) {
			System.out.println(result);
		} else {
			System.out.println(-1);
		}
	}
}
