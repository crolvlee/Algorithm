import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution {
    static int N;
    static int[][] ground;
    static int answer;
    static Set<Integer> numSet;

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= T; tc++) {
//            if (tc >=2) continue;

            // 1. 입력받기
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            ground = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    ground[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 2. 시작점 설정해서 다이아몬드로 이동
            answer = -1;
            for (int i = 0; i <= N-3; i++) {
                for (int j = 1; j <= N-2; j++) {
                    numSet = new HashSet<>();
                    numSet.add(ground[i][j]);
                    DFS(i, j, i, j, 0, 0, 0, 1);
                }
            }

            System.out.println("#" + tc + " " + answer);
        }
    }

    static void DFS(int topRow, int topCol, int nowRow, int nowCol, int nowDir, int a, int b, int depth) {

        if (nowDir == 0) {
            // 1. 같은 방향
            int nextRow1 = nowRow + 1;
            int nextCol1 = nowCol + 1;

            if (0 <= nextRow1 && nextRow1 <= N-1 && 0 <= nextCol1 && nextCol1 <= N-1) {
                if (!numSet.contains(ground[nextRow1][nextCol1])) {
                    numSet.add(ground[nextRow1][nextCol1]);
                    DFS(topRow, topCol, nextRow1, nextCol1, nowDir, a, b, depth + 1);
                    numSet.remove(ground[nextRow1][nextCol1]);
                }
            }

            // 2. 다른 방향
            if (topRow == nowRow && topCol == nowCol) {
                return;
            }

            int nextRow2 = nowRow + 1;
            int nextCol2 = nowCol - 1;

            if (0 <= nextRow2 && nextRow2 <= N-1 && 0 <= nextCol2 && nextCol2 <= N-1) {
                if (!numSet.contains(ground[nextRow2][nextCol2])) {
                    int aNew = nowCol - topCol;
                    numSet.add(ground[nextRow2][nextCol2]);
                    DFS(topRow, topCol, nextRow2, nextCol2, 1, aNew, b, depth + 1);
                    numSet.remove(ground[nextRow2][nextCol2]);
                }
            }

        } else if (nowDir == 1) {
            // 1. 같은 방향
            int nextRow1 = nowRow + 1;
            int nextCol1 = nowCol - 1;

            if (0 <= nextRow1 && nextRow1 <= N-1 && 0 <= nextCol1 && nextCol1 <= N-1) {
                if (!numSet.contains(ground[nextRow1][nextCol1])) {
                    numSet.add(ground[nextRow1][nextCol1]);
                    DFS(topRow, topCol, nextRow1, nextCol1, nowDir, a, b, depth + 1);
                    numSet.remove(ground[nextRow1][nextCol1]);
                }
            }

            // 2. 다른 방향
            int nextRow2 = nowRow - 1;
            int nextCol2 = nowCol - 1;

            if (0 <= nextRow2 && nextRow2 <= N-1 && 0 <= nextCol2 && nextCol2 <= N-1) {
                if (!numSet.contains(ground[nextRow2][nextCol2])) {
                    int bNew = nowRow - topRow - a;
                    numSet.add(ground[nextRow2][nextCol2]);
                    DFS(topRow, topCol, nextRow2, nextCol2, 2, a, bNew, depth + 1);
                    numSet.remove(ground[nextRow2][nextCol2]);
                }
            }

        } else if (nowDir == 2) {
            if (nowRow == topRow + b) { // 좌측 꼭짓점에 도달한 경우
                int nextRow = nowRow - 1;
                int nextCol = nowCol + 1;

                if (nextRow == topRow && nextCol == topCol) { // 다음점이 시작점인 경우
                    answer = Math.max(answer, depth);
                    return;
                }

                if (0 <= nextRow && nextRow <= N-1 && 0 <= nextCol && nextCol <= N-1) {
                    if (!numSet.contains(ground[nextRow][nextCol])) {
                        numSet.add(ground[nextRow][nextCol]);
                        DFS(topRow, topCol, nextRow, nextCol, 3, a, b, depth + 1);
                        numSet.remove(ground[nextRow][nextCol]);
                    }
                }

            } else {
                int nextRow = nowRow - 1;
                int nextCol = nowCol - 1;

                if (0 <= nextRow && nextRow <= N-1 && 0 <= nextCol && nextCol <= N-1) {
                    if (!numSet.contains(ground[nextRow][nextCol])) {
                        numSet.add(ground[nextRow][nextCol]);
                        DFS(topRow, topCol, nextRow, nextCol, 2, a, b, depth + 1);
                        numSet.remove(ground[nextRow][nextCol]);
                    }
                }
            }

        } else {
            int nextRow = nowRow - 1;
            int nextCol = nowCol + 1;

            // 1. 시작점(topRow, topCol)에 도달했는지 확인
            if (nextRow == topRow && nextCol == topCol) {
                answer = Math.max(answer, depth);
                return; // 사각형 완성!
            }

            // 2. 시작점이 아니라면 계속 해당 방향으로 직진
            if (nextRow >= 0 && nextRow < N && nextCol >= 0 && nextCol < N) {
                if (!numSet.contains(ground[nextRow][nextCol])) {
                    numSet.add(ground[nextRow][nextCol]);
                    DFS(topRow, topCol, nextRow, nextCol, 3, a, b, depth + 1);
                    numSet.remove(ground[nextRow][nextCol]);
                }
            }
        }
    }
}