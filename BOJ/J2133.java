/*
REDO 
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J2133 {
    static int n;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+1];
        if(n%2==1){
            System.out.println(0);
            return;
        }
        dp[0] = 1;
        dp[2] = 3;
        for(int i=4; i<=n; i+=2){
            dp[i] += dp[i-2]*3;
            for(int j=4; j<=i; j+=2){
                dp[i]+= dp[i-j]*2;
            }
        }
        System.out.println(dp[n]);
    }
}
