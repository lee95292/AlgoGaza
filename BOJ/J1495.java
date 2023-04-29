package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class J1495 {
    static int NOT_EXIST = 2000;
    static int[][] dp;
    static int[] v;
    static int n,m;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        dp = new int[n][1001];
        // for(int[] d: dp){
        //     Arrays.fill(d,NOT_EXIST);
        // }
        v = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<v.length; i++){
            v[i] = Integer.parseInt(st.nextToken());
        }

        solve(0, s);
        for(int i=m; i>=0; i--){
            if(dp[n-1][i] == 1){
                System.out.println(i);
                return;
            }
        }
        System.out.println("-1");
        
    }

    public static void solve(int turn, int prev){
        if(turn == n) return;
        int up = prev + v[turn];
        int down = prev - v[turn];
        // System.out.println(up+" "+down);
        if(up <= m && dp[turn][up] == 0) {
            dp[turn][up] = 1;
            solve(turn+1, up);
        }
        if(down >= 0 && dp[turn][down] == 0) {
            dp[turn][down] = 1;
            solve(turn+1, down);
        }
    }
    
}
