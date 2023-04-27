package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class J2156 {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        int[] arr = new int[n];
        int[][] dp = new int[n][3];
        int answer = 0;
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(br.readLine());
            dp[i][0] = arr[i];
        }
        if(n <= 2){
            int ans = 0;
            for(int i : arr){ ans += i;}
            System.out.println(ans);
            return;
        }
        dp[0][1] = arr[0];
        dp[1][1] = arr[1];
        for(int i=1; i<n; i++){
            if (i>2) dp[i][0] = arrmax(dp[i-3]) + arr[i];
            if (i>1) dp[i][1] = arrmax(dp[i-2]) + arr[i];
            dp[i][2] = Math.max(dp[i-1][1], dp[i-1][0]) + arr[i];
            answer = Math.max(arrmax(dp[i]), answer);
            // printdp(dp);
        }

        System.out.println(answer);
        
    }

    public static int arrmax(int[] arr){
        int max = -1;
        for(int i=0; i<arr.length; i++){
            if(max < arr[i]) max =arr[i];
        }
        return max;
    }

    public static void printdp(int[][] dp){
        for(int i=0; i<dp.length; i++){
            System.out.println(Arrays.toString(dp[i]));
        }

        System.out.println();
    }
}
