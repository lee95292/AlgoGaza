package others.softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class S390 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int[] rocks = new int [n];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            rocks[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(Solution(n,rocks));
    }
    public static int Solution(int n , int[] rocks){
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for(int i=1; i<n; i++){
            for(int j=0; j<i; j++){
                if(rocks[i] < rocks[j]) continue;
                dp[i] = Math.max(dp[i], dp[j]+1);
            }
        }

        int m = 0;
        for(int i:dp){
            m = Math.max(m,i);
        }
        // System.out.println(Arrays.toString(dp));
        return m;
    }
}
