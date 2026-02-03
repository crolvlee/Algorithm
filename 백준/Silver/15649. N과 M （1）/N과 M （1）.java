import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int N;
	static int M;
	static boolean[] visited;
	static String[] combination_path;

	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] line = br.readLine().split(" ");
		N = Integer.parseInt(line[0]);
		M = Integer.parseInt(line[1]);
		
		visited = new boolean[N+1];
		combination_path = new String[M];
		
		permutation(0);
		
	}
	
	private static void permutation(int depth) {
		if (depth == M) {
			System.out.println(String.join(" ", combination_path));
			return;
		}
		
		for (int i = 1; i < N+1; i++) {
			if (visited[i] == false) {
				combination_path[depth] = Integer.toString(i);
				visited[i] = true;
				permutation(depth + 1);
				combination_path[depth] = "0";
				visited[i] = false;
			}
		}
	}

}
