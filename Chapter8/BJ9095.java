package dp;

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class BJ9095 {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		int[] dp = new int[12];
		
		dp[1]=0+1;
		dp[2]=1+1;
		dp[3]=3+1;
//		dp4=7
//		dp5=13
//		dp6=24
//		dp7=44
		for(int i=4;i<12;i++) {
			dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
		}
		
		for(int i=0;i<t;i++) {
			int k = Integer.parseInt(br.readLine());
			System.out.println(dp[k]);
		}

	}

}
