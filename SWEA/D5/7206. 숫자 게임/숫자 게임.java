import java.io.*;
import java.util.*;

public class Solution {
    static int[] divideIdx;
    static int maxDepth;
    static List<Integer> multifliedNums;
    static Map<Integer, Integer> numMaxDepth;

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= T; tc++) {
            st =  new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            maxDepth = 0;
            numMaxDepth = new HashMap<>();

            int r = DFS(N, 0);

            System.out.println("#" + tc + " " + maxDepth);
        }
    }

    static int DFS(int nowNum, int nowDepth) {
        if (nowNum < 10) {
            maxDepth =  Math.max(nowDepth, maxDepth);
            return nowDepth;
        }

        // 현재 숫자를 나눠서 만들 수 있는 숫자들(multifliedNums) 구하기
        int nowNumCnt = Integer.toString(nowNum).length();
        divideIdx = new int[nowNumCnt];
        multifliedNums = new ArrayList<>();
        divide(nowNum, nowNumCnt - 1, 0);

        List<Integer> nextNums = new ArrayList<>(multifliedNums);
        int bestDepthFromHere = nowDepth;

        for (int multifliedNum : nextNums) {
            int resultDepth;
            if (numMaxDepth.containsKey(multifliedNum)) { // 앞에서 나온 숫자인 경우
                resultDepth = numMaxDepth.get(multifliedNum) + nowDepth  + 1;
                maxDepth = Math.max(resultDepth, maxDepth);
            } else { // 앞에서 나온 숫자가 아닌 경우
                resultDepth =  DFS(multifliedNum, nowDepth + 1);
            }

            bestDepthFromHere = Math.max(bestDepthFromHere, resultDepth);
        }

        numMaxDepth.put(nowNum, bestDepthFromHere - nowDepth);
        return bestDepthFromHere;
    }

    static void divide(int nowNum, int nowNumCnt, int pos) {
        if (pos == nowNumCnt) {
            List<Integer> dividedNums = new ArrayList<>();
            String currentNum = "";

            for (int i = 0; i < nowNumCnt; i++) {
                currentNum += Integer.toString(nowNum).substring(i, i+1);
                if (divideIdx[i] == 1) {
                    dividedNums.add(Integer.parseInt(currentNum));
                    currentNum = "";
                }
            }

            String lastNum = Integer.toString(nowNum).substring(nowNumCnt);
            if (!currentNum.isEmpty()) {
                dividedNums.add(Integer.parseInt(currentNum + lastNum));
            } else {
                dividedNums.add(Integer.parseInt(lastNum));
            }

            int result = dividedNums.stream().reduce(1, (a, b) -> a  * b);
            if (result != nowNum) {
                multifliedNums.add(result);
            }

            return;
        }

        divideIdx[pos] = 0;
        divide(nowNum, nowNumCnt, pos + 1);
        divideIdx[pos] = 1;
        divide(nowNum, nowNumCnt, pos + 1);
    }
}