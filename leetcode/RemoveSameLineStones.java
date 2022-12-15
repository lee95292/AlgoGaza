import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class RemoveSameLineStones {

	public static void main(String[] args) {
		int[][] stones = {{0,0},{0,1},{1,0},{1,2},{2,1},{2,2}};
		System.out.println(solution(stones));
	}
	public static int solution(int[][] stones){
		int[] visit = new int[stones.length];
		

		for(int i=0; i< stones.length; i+=1){
			if(visit[i] == 1) continue;

			
		}
		return stones.length;
	}
}