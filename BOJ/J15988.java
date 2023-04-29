/*
 * 1,2,3 더하기 3
 * 간단한 규칙찾기 DP. 항상 시작경계값 체크하고, 모듈러 있을경우 개별 연산이 모듈러 값 넘어가는지 체크
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class J15988 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        List<Integer> ans = new ArrayList<>();
        int maxa = 0;
        for(int i=0; i<T; i++){
            int n = Integer.parseInt(br.readLine());
            ans.add(n);
            if(maxa < n) maxa = n;
        }
        int[] dp = new int[maxa+10];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        
        for(int i=4; i<=maxa; i++){
            dp[i] = ((dp[i-1] + dp[i-2])%1000000009 + dp[i-3])%1000000009;
        }

        for( Integer a : ans){
            System.out.println(dp[a]);
        }
    }
}
