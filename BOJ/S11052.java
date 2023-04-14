package BOJ;
import java.io.*;

public class S11052{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] prices = br.readLine().split(" ");
        int[] dp = new int[N+1];
        for(int i=0; i<N; i++){
            dp[i+1] = Integer.parseInt(prices[i]);
        }
        for(int i=1; i< N+1; i++){
            for(int j=1; j<=i; j++){
                dp[i] = Math.max(dp[i], dp[i-j] + dp[j]);
            }
        }
        System.out.println(dp[N]);
    }
}