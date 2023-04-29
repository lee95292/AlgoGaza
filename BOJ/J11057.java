package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J11057 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader( System.in) );
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[n+1][10];

        Arrays.fill(dp[1], 1);
        for(int i=2; i<=n; i++){
            for(int j=0;j<10;j++){
                for(int k=j; k<10; k++){
                    dp[i][j] = (dp[i-1][k]+dp[i][j])%10007;
                }
            }
        }
        int answer = 0;
        for(int i=0; i<10; i++){
            answer = (dp[n][i] + answer)%10007;
        }

        System.out.println(answer);

    }
    
}
