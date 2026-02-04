import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		DFS(0, 0, N);
	}
	
	
	private static void DFS(int num, int depth, int N) {
		if (depth == N) {
			System.out.println(num);
			return;
		}
		
		for (int i = 0; i <= 9; i++) {
			int nextNum = 10 * num + i;
			if (isPrime(nextNum)) {
				DFS(nextNum, depth+1, N);
			}
		}
		
		return;
	}
	
	
	private static boolean isPrime(int num) {
		if (num == 1 || num == 0) {
			return false;
		}
		
		int s = (int) Math.pow(num, 1.0 / 2);
		boolean isPrime = true;
		
		for (int i = 2; i <= s; i++) {
			if (num % i == 0) {
				isPrime = false;
				break;
			}
		}
		
		return isPrime;
	}
}
