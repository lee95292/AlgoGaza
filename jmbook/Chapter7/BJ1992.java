package Chapter7;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/*
 * �ѹ��� Ǯ�� ���� ���� - �ڹ� �÷��� ���� ����� ����
 * 
 * �÷����� ���, �޸𸮻� �ѹ� �����Ǹ� subList �޼��带 ����ص�, ���� �ִ� ����Ʈ���� �޸� �ּҸ� ����� (������� ����)
 * ����, new Ű���带 ���� ���� �����ؾ� �Ѵ�.
 * */

public class BJ1992 {

	public static void main(String[] args) throws Exception{
			BufferedReader br =new BufferedReader(new InputStreamReader(System.in));

			int n = Integer.parseInt(br.readLine());
			String[] inpRow = null;
			
			List<List<Integer>> data = new ArrayList<List<Integer>>();
			
			for(int i=0;i<n;i++){
				inpRow=br.readLine().split("");
				List<Integer> row = new ArrayList<Integer>();
				
				for(int j=0;j<n;j++) {
					row.add(Integer.parseInt(inpRow[j]));
				}
				data.add(row);		
			}
			
			System.out.println(printQuadTree(n, data));
	}
	public static String printQuadTree(int width,List<List<Integer>> data) {
		if(width==1) {
			return data.get(0).get(0).toString();
		}
		if(!isContain(1,data)) {
			return "0";
		}else if(!isContain(0, data)) {
			return "1";
		}else {
			List<List<Integer>> data1_1= new ArrayList<List<Integer>>(data.subList(0, width/2));
			List<List<Integer>> data1_2= new ArrayList<List<Integer>>(data.subList(0, width/2));
			List<List<Integer>> data2_1= new ArrayList<List<Integer>>(data.subList(width/2,width));
			List<List<Integer>> data2_2= new ArrayList<List<Integer>>(data.subList(width/2,width));
			
			for(int i=0;i<width/2;i++) {
				data1_1.set(i, data1_1.get(i).subList(0, width/2));
				data1_2.set(i, data1_2.get(i).subList(width/2, width));
				data2_1.set(i, data2_1.get(i).subList(0, width/2));
				data2_2.set(i, data2_2.get(i).subList(width/2, width));			
			}
			
			return "("+printQuadTree(width/2, data1_1)+printQuadTree(width/2, data1_2)+printQuadTree(width/2, data2_1)+printQuadTree(width/2, data2_2)+")";
		}
	}
	public static boolean isContain(int number,List<List<Integer>> data) {
		boolean result=false;
		
		for(int i=0;i<data.size();i++) {
			if(data.get(i).contains(number)) {
				return true;
			}
		}
			
		return result;
	}

}
