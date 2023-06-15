package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J11985 {
    static int n, m, k;
    static long[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] inp = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        n = inp[0];
        m = inp[1];
        k = inp[2];
        long[] arr = new long[n+1];
        dp = new long[n+1];
        Arrays.fill(dp, Long.MAX_VALUE);
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            long minVal = Long.MAX_VALUE, maxVal = Long.MIN_VALUE;
            for(int j=1; j<=m && i-j >=0 ; j++){
                maxVal = Math.max(maxVal, arr[i-j+1]);
                minVal = Math.min(minVal, arr[i-j+1]);
                dp[i] = Math.min(dp[i], dp[i-j] + j*(maxVal - minVal) + k);
            }
        }
        // System.out.println(Arrays.toString(dp));
        System.out.println(dp[n]);

    }

}

