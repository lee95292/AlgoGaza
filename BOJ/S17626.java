package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class S17626{
    static int[] dp;
    static int MAX_DP = 50001;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n  = Integer.parseInt(br.readLine());
        
        dp = new int[MAX_DP];
        Arrays.fill(dp,MAX_DP);
        for(int i=0; i<= Math.sqrt(n); i++){
            dp[i*i]=1;
        }
        for(int i=1; i<=n; i++){
            if(dp[i]==1)
                continue;

            for(int j=1 ; j<= Math.sqrt(i);j++){
                dp[i] = Math.min(dp[i], dp[j*j] + dp[i-j*j]);
            }
        }
        System.out.println(dp[n]);
    }
    

    public static int sqrtPow(int x){
        return (int)Math.pow(Math.floor(Math.sqrt(x)),2);
    }
}