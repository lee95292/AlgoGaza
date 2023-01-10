package Chapter7;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//�����̸� : Z
public class BJ1074 {
	static int x;
	static int y;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n= Integer.parseInt(st.nextToken());
		int y= Integer.parseInt(st.nextToken());
		int x= Integer.parseInt(st.nextToken());
		System.out.println(calculateTurn(n, x, y));
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<0;j++) {
				System.out.print(calculateTurn(n, i, j)+" ");
			}
			System.out.println();
		}
	}
	
	static int calculateTurn(int n,int x,int y) {
		if(n==0) {
			return 0;
		}
		int xDivide = (int)Math.pow(2, n)/2;
		int yDivide = (int)Math.pow(2, n)/2;
		
		int divideNumber=0;
		if(x<xDivide&&y<yDivide) {
			divideNumber=0;
		}else if(x>=xDivide&&y<yDivide) {
			divideNumber=1;
			x-=xDivide;
		}else if(x<xDivide&&y>=yDivide) {
			divideNumber=2;
			y-=yDivide;
		}else if(x>=xDivide&&y>=yDivide) {
			divideNumber=3;
			y-=yDivide;
			x-=xDivide;
		}
		
		return (int)Math.pow(2, 2*n-2)*divideNumber+calculateTurn(n-1, x, y);
	}

}
