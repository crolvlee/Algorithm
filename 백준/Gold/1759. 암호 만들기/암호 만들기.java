import java.io.FileInputStream;
import java.util.*;

public class Main {
    static int L;
    static int C;
    static String[] alphabet;
    static String[] moeum_arr = {"a", "e", "i", "o", "u"};
    static int[] combination_path;
    static List<int[]> combination_list = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        // 1. 입력받기
        //System.setIn(new FileInputStream("res/input.txt"));
        Scanner sc = new Scanner(System.in);

        L = sc.nextInt();
        C = sc.nextInt();
        sc.nextLine();

        alphabet = sc.nextLine().split(" ");
        Arrays.sort(alphabet);

        combination_path = new int[L];

        // 2. 인덱스 이중리스트 만들기
        combination(0, 0);

        // 3. 인덱스 순열 돌면서, 가능한 암호 프로그램 찾기
        for (int[] combi : combination_list) {
            int moeum_cnt = 0;
            int jaeum_cnt = 0;

            for (int c : combi) {
                String now_alphabet = alphabet[c];
                if (now_alphabet.equals("a") || now_alphabet.equals("e") || now_alphabet.equals("i") || now_alphabet.equals("o") || now_alphabet.equals("u")) {
                    moeum_cnt += 1;
                } else {
                    jaeum_cnt += 1;
                }
            }

            if (moeum_cnt >= 1 && jaeum_cnt >= 2) {
                for (int idx : combi) {
                    System.out.print(alphabet[idx]);
                }
                System.out.println();
            }
        }
    }

    private static void combination(int depth, int start) {
        if (depth == L) {
            combination_list.add(combination_path.clone());
            return;
        }

        for (int i = start; i < C; i++) {
            combination_path[depth] = i;
            combination(depth+1, i+1);
            combination_path[depth] = 0;
        }
    }
}