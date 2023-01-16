package others.softeer;

import java.util.*;
import java.io.*;

public class S654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        int[] info = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int v = Integer.parseInt(st.nextToken());
            info[i] = v;
        }
        System.out.println(Solution(n, info));

    }

    public static long Solution(int n, int[] info) {
        int[][] dp = new int[n+1][n+1]; //I보다 오른쪽에 있는 수들 중 J보다 작은 수
        for (int i = n-1; i>=0; i--) {
            for (int j = 1; j <= n; j++) {
                dp[j][i] = dp[j][i+1];
                if (info[i] < j) {
                    dp[j][i]++;
                }
            }
        }
        long answer=0;
        for(int i=0; i<n; i++){
            for(int j=i;j<n;j++){
                if(info[i] < info[j]){
                    answer += dp[info[i]][j];
                }
            }
        }
        return answer;
    }
}