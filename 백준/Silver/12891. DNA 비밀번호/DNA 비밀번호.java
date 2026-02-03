import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		// 1. 입력받기
		st = new StringTokenizer(br.readLine());
		int S = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		String word = st.nextToken();
		
		st = new StringTokenizer(br.readLine());
		int[] arr = new int[4]; // A, C, G, T
		for (int i = 0; i < 4; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		// 2. 슬라이딩 배열 초기화
		Map<String, Integer> map = new HashMap<>();
		map.put("A", 0);
		map.put("C", 0);
		map.put("G", 0);
		map.put("T", 0);
		
		for (int i = 0; i < P; i++) {
			String now = word.substring(i, i+1);
			map.put(now, map.get(now) + 1);
		}
			
		// 3. 슬라이딩
		int answer = 0;
		for (int i = 0; i <= S-P; i++) {
			if (i >= 1) {
				String prev = word.substring(i - 1, i);
				String next = word.substring(i + P - 1, i + P);
				
				map.put(prev, map.get(prev) - 1);
				map.put(next, map.get(next) + 1);
			}
			
			int cntA = map.get("A");
			int cntC = map.get("C");
			int cntG = map.get("G");
			int cntT = map.get("T");
						
			if (cntA >= arr[0] && cntC >= arr[1] && cntG >= arr[2] && cntT >= arr[3]) {
				answer += 1;
			}
		}
		
		System.out.println(answer);
	}
}
