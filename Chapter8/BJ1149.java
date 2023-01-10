
import java.util.Scanner;

public class BJ1149 {
	public static void main(String args[])throws Exception {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] cost = new int[n][3];
		int[][] dp = new int[n+1][3];
		
		for(int i=0;i<n;i++) {
			cost[i][0]=sc.nextInt();
			cost[i][1]=sc.nextInt();
			cost[i][2]=sc.nextInt();
		}
		
		dp[0][0]=cost[0][0];
		dp[0][1]=cost[0][1];
		dp[0][2]=cost[0][2];
		
		for(int i=1;i<n;i++) {
			dp[i+1][0]=1000;
			dp[i+1][1]=1000;
			dp[i+1][2]=1000;
			
			dp[i][0]=cost[i][0]+min(dp[i-1][1],dp[i-1][2]);
			dp[i][1]=cost[i][1]+min(dp[i-1][0],dp[i-1][2]);
			dp[i][2]=cost[i][2]+min(dp[i-1][1],dp[i-1][0]);
				
		}
		System.out.println(min(min(dp[n-1][0],dp[n-1][1]),dp[n-1][2]));
	}
	
	static int min(int a,int b) {
		if(a>b)
			return b;
		else
			return a;
	}
}
  