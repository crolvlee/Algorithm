import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;

public class Main {
	static int N;
	static int M;
	static String[] combination_path;

	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] line = br.readLine().split(" ");
		N = Integer.parseInt(line[0]);
		M = Integer.parseInt(line[1]);
		combination_path = new String[M];
		
		combination(0, 0);
		
	}
	
	static void combination(int start, int depth) {
		if (depth == M) {
			System.out.println(String.join(" ", combination_path));
			return;
		}
		
		for (int i = start + 1; i < N + 1; i++) {
			combination_path[depth] = Integer.toString(i);
			combination(i, depth + 1);
			combination_path[depth] = "0";
		}
	}
}
