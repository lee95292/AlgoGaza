package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J2116 {

    public static void main(String[] args) throws IOException {
        boolean debug = false;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] dp = new int[n][6]; // x층에서 y가 밑으로 깔릴 때, 옆면합
        int[][] dice = new int[n][6];
        int[][] diceMap = new int[][] { { 0, 5 }, { 5, 0 }, { 1, 3 }, { 2, 4 }, { 3, 1 }, { 4, 2 } };
        for (int i = 0; i < n; i++) {
            dice[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)-1).toArray();
        }

        for (int i = 0; i < n; i++) {
            for (int[] dm : diceMap) {
                if (dice[i][dm[0]] == 6 || dice[i][dm[1]] == 6)
                    System.out.println(dm[0] + " " + dm[1]);
                for (int j = 0; j < 6; j++) {
                    int down = dice[i][dm[0]], up = dice[i][dm[1]];
                    if (dice[i][j] != down && dice[i][j] != up) {
                        int v = dice[i][j];
                        if (i > 0)
                            v += dp[i - 1][up];
                        dp[i][down] = Math.max(dp[i][down], v);
                    }
                }
            }
        }
        if (debug) {
            for (int i = 0; i < n; i++) {
                System.out.println(Arrays.toString(dp[i]));
            }
        }
        int answer = 0;
        for (int i = 0; i < 6; i++) {
            answer = Math.max(dp[n - 1][i], answer);
        }
        System.out.println(answer+n);

    }

}
