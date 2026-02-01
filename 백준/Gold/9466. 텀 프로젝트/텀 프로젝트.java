import java.io.*;
import java.util.*;

public class Main {
    private static int[] endNodes;
    private static int[] team; // -1: 팀에 속하지 X / 0: 순회 전 / 1: 팀에 속함 / 2: 재귀 진행 중

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            // 1. 입력받기 + 초기화
            int n = Integer.parseInt(br.readLine());
            endNodes = new int[n + 1];

            st = new StringTokenizer(br.readLine());
            for (int i = 1; i < n + 1; i++) {
                endNodes[i] = Integer.parseInt(st.nextToken());
            }

            team = new int[n + 1];

            // 2. 노드 순회
            for (int nowNode = 1; nowNode < n + 1; nowNode++) {
                if (team[nowNode] == 0) {
                    team[nowNode] = 2;
                    recursion(new ArrayList<>(List.of(nowNode)));
                    //System.out.println(Arrays.toString(team));
                }
            }

            // 3. 답 출력
            int answer = 0;
            for (int i = 1; i < n + 1; i++) {
                if (team[i] == -1) {
                    answer += 1;
                }
            }

            System.out.println(answer);
        }
    }

    private static void recursion(List<Integer> list) {
        int nowNode = list.get(list.size() - 1);
        int nextNode = endNodes[nowNode];

        if (team[nextNode] == 2) {
            int prevSameNodeIdx = list.indexOf(nextNode);

            // 팀에 속하는지 여부를 넣어주기
            for (int i = 0; i < prevSameNodeIdx; i++) {
                int node = list.get(i);
                team[node] = -1;
            }

            for (int i = prevSameNodeIdx; i < list.size(); i++) {
                int node = list.get(i);
                team[node] = 1;
            }

            return;
        } else if (team[nextNode] == 0) {
            team[nextNode] = 2;
            list.add(nextNode);
            recursion(list);

            return;
        }

        for (int node : list) {
            team[node] = -1;
        }
    }
}