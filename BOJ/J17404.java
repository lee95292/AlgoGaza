package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class J17404 {
    static int[][] dp,price;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        dp = new int[n][3];
        price = new int[n][3];
        for(int i=0 ;i< n; i++){
            price[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        }
        dp[0][0] = price[0][0];
        dp[0][1] = price[0][1];
        dp[0][2] = price[0][2];
        for(int i=1; i<n; i++){
            System.out.println(Arrays.toString(price[i]));
            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + price[i][0];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + price[i][1];
            dp[i][2] = Math.min(dp[i-1][1], dp[i-1][0]) + price[i][2];
        }
        
        dp[0][0] = Math.min(dp[n-1][1], dp[n-1][2]) + price[0][0];
        dp[0][1] = Math.min(dp[n-1][0], dp[n-1][2]) + price[0][1];
        dp[0][2] = Math.min(dp[n-1][1], dp[n-1][0]) + price[0][2];
        System.out.println(Arrays.toString(dp[0]));
    }
    
}
