package Chapter6;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * ���� : ���Ⱓ�� ����� �ְ�, ����� ���� ���� ���� �� �ִ� ������ ã��. (����Ž��)
 * �ѹ��� Ǯ�� ���� ����  : ������� ����� üũ ����
 * */

public class BJ14501 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n=sc.nextInt();
		ArrayList<Integer> t = new ArrayList<Integer>(n);
		ArrayList<Integer> p = new ArrayList<Integer>(n);
		
		for(int i=0;i<n;i++) {
			t.add(sc.nextInt());
			p.add(sc.nextInt());
		}
		sc.close();
		System.out.println(bestSchedule(t, p));
	}
	
	public static Integer bestSchedule(List<Integer> t,List<Integer> p) {
		if(t.size()==0) {			
			return 0;
		}
		if(t.size()==1) {
			return t.get(0)==1?p.get(0):0;
		}
		Integer jumpToNextDay =bestSchedule(t.subList(1, t.size()), p.subList(1, p.size()));
		Integer consultToday=0;
		
		if(t.get(0)<=t.size()) {			
			consultToday = p.get(0)+bestSchedule(t.subList(t.get(0), t.size()),p.subList(t.get(0), p.size()));
		}
		return jumpToNextDay>consultToday?jumpToNextDay:consultToday;
	}
}
