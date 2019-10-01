package bruteforce;

import java.util.Scanner;

/*
 * 한번에 풀지 못한 이유
 * 1. 일반적인 규칙을 찾는것에만 집중하고, 예외사항(10~99까지의 숫자에 대해서는 모두 한수)를 생각하지 않음.
 * 2. 그냥 감  떨어짐
 * */
public class BJ1065 {

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.close();

		int result=0;
		
			for(int i=1;i<=n;i++) {		
				if(isHansu(i)) {
	//				System.out.println("hansu");
					result++;
				}
			}
		System.out.println(result);
		
	}
	
	public static boolean isHansu(int i) {
		boolean result=true;
		
	
		int sequence=(i/10)%10-i%10;
//		System.out.println(i+", seq:"+sequence);
		while(i>=10) {
			if((i/10)%10-i%10!=sequence) {				
				result=false;
				break;
			}
			i=i/10;			
		}
		return result;
	}
}

