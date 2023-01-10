package Chapter6;

import java.util.Scanner;

/*
 * �ѹ��� Ǯ�� ���� ����
 * 1. �Ϲ����� ��Ģ�� ã�°Ϳ��� �����ϰ�, ���ܻ���(10~99������ ���ڿ� ���ؼ��� ��� �Ѽ�)�� �������� ����.
 * 2. �׳� ��  ������
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

