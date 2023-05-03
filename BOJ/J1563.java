/*
1563, DP 
경우의 수 꼼꼼히 세는 문제. 
결석 연속 3회 안되고, 지각 2회 안됨
State( Late, Absent )로 Bottom-up DP
 */

package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class J1563 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int mod = 1000000;
        int n = Integer.parseInt(br.readLine());
        int[][][] dp = new int[n+1][2][3];
        dp[1][1][0] = 1;
        dp[1][0][1] = 1;
        dp[1][0][0] = 1;

        for(int i=2; i<=n; i++){
            dp[i][0][0]= ((dp[i-1][0][0] +dp[i-1][0][1]) % mod + dp[i-1][0][2])%mod;
            dp[i][1][0]= (((((dp[i-1][1][0]+ + dp[i-1][0][1]) % mod + dp[i-1][0][0])% mod +dp[i-1][0][2])% mod +dp[i-1][1][1])% mod + dp[i-1][1][2])% mod;
            
            dp[i][0][1]= dp[i-1][0][0] ;
            dp[i][1][1]= dp[i-1][1][0] ;

            dp[i][0][2]= dp[i-1][0][1];
            dp[i][1][2]= dp[i-1][1][1];
            // for(int k=0; k<2; k++){
            //     System.out.println(Arrays.toString(dp[i][k]));
            // }
            // System.out.println();
        }

        int answer = 0;
        for(int i=0; i<2; i++){
            for(int j=0; j<3; j++){
                answer = (dp[n][i][j] + answer)%mod;
            }
        }

        System.out.println(answer);

    }
    
}
