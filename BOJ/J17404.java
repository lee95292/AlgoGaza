/*
REDO
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class J17404 {
    static int[][] dp, price;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        dp = new int[n][3];
        price = new int[n][3];
        for (int i = 0; i < n; i++) {
            price[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        }

        int answer = 1000001;
        for (int k = 0; k < 3; k++) {
            for(int i=0; i<3; i++){
                dp[0][i] = 1000001;
            }
            dp[0][k] = price[0][k];
            for (int i = 1; i < n; i++) {
                dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + price[i][0];
                dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + price[i][1];
                dp[i][2] = Math.min(dp[i - 1][1], dp[i - 1][0]) + price[i][2];
            }
            dp[n - 1][k] = Integer.MAX_VALUE;

            for(int i=0; i<3; i++){
                answer = Math.min(dp[n-1][i], answer);
            }
            dp[0][k] = 0;
        }
        System.out.println(answer);
    }

}

