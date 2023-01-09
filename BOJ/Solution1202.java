package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution1202 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] jewels = new int[n][2];
        int[] capacities = new int[k];

        for(int i=0; i<n; i+=1){
            st = new StringTokenizer(br.readLine());
            jewels[i][0] = Integer.parseInt(st.nextToken());
            jewels[i][1] = Integer.parseInt(st.nextToken());
            
        }
        for(int i=0; i<k; i+=1){
            capacities[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(Solution(n,k,jewels,capacities));
    }

    public static long Solution(int n, int k, int[][] jewels, int[] capacities) {
        long answer = 0;

        PriorityQueue<Map<Integer, Integer>> pq = new PriorityQueue<>((Map<Integer, Integer>  m1, Map<Integer, Integer>   m2) -> {
        });
        
        return answer;
    }

}

