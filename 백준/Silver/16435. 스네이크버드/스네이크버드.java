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
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int[] hArr = new int[N];
		for (int i = 0; i < N; i++) {
			hArr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(hArr);
		
		int nowL = L;
		
		for (int h : hArr) {
			if (h <= nowL) {
				nowL += 1;
			} else {
				break;
			}
		}
		
		System.out.println(nowL);
	}
}
