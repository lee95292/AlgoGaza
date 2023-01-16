package Chapter6;

import java.util.Arrays;
import java.util.Scanner;

public class BJ2309 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tall[]= new int[9];
		int sum=0;
		
		for(int i=0;i<9;i++) {
			tall[i]=sc.nextInt();
			sum+=tall[i];
		}
//		System.out.println(sum);
		Arrays.sort(tall);
		sc.close();
		
		boolean breakflag=false;
		
		int not1=0,not2=0;
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				if(sum-tall[i]-tall[j]==100&&i!=j) {
					not1=i;
					not2=j;
					break;
				}
				
				
			}
			if(breakflag) {
				break;
			}
		}
		
		for(int i=0;i<9;i++) {
			if(i!=not1&&i!=not2)
			System.out.println(tall[i]);
		}
	}

}
