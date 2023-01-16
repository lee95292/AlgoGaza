package Chapter7;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ1780 {

	static int minusOne;
	static int zero;
	static int one;
	
	public static void calculateNumber(Integer[][] paper, int n,int x,int y) {
		if(n==1) {
			if(paper[y][x]==-1)minusOne++;
			if(paper[y][x]==0)zero++;
			if(paper[y][x]==1)one++;
			return;
		}
		Integer singleNum=singleNumber(paper, n, x, y);
		if(singleNum!=-2) {
			if(singleNum==-1)minusOne++;
			if(singleNum==0)zero++;
			if(singleNum==1)one++;
			return;
		}
		int quoter= n/3;
		for(int i=0;i<3;i++) {
			for(int j=0;j<3;j++) {
				calculateNumber(paper, quoter, x+j*quoter, y+i*quoter);
			}
		}
	}
	
	public static Integer singleNumber(Integer [][] paper, int n,int x,int y) {
		Integer prev= paper[y][x];
		for(int i=y;i<y+n;i++) {
			for(int j=x;j<x+n;j++) {
				if(prev!=paper[i][j]) {
					return -2;
				}
				prev=paper[i][j];
			}
		}
		return prev;
	}
	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n =Integer.parseInt(br.readLine());
		String[] paperStringType = new String[n];
		Integer [][] paper= new Integer[n][n];
		
		for(int i=0;i<n;i++) {
			paperStringType=br.readLine().split(" ");
			
			paper[i]=Arrays.stream(paperStringType).map(x->{return Integer.parseInt(x);}).toArray(Integer[]::new);
		}
		
		calculateNumber(paper, n, 0, 0);
		
		System.out.println(minusOne);
		System.out.println(zero);
		System.out.println(one);
		
		
	}

}
