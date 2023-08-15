package Tips;

import java.util.Arrays;

public class BubbleSort{
  public static void main(String[] args){
		int[] array = new int[]{5,3,2,7,1,4,6};
		int n = 7;
		for(int k=n-1; k>0; k--){
			for(int r=0; r<k; r++){
				if(array[r] > array[r+1]){
					int tmp = array[r];
					array[r] = array[r+1];
					array[r+1] = tmp;
				}
			}
		}
		System.out.println(Arrays.toString(array));

	}
}