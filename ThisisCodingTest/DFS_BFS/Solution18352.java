package DFS_BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution18352 {
    private static int n;
    private static int m;
    private static int k;
    private static int x;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken())-1;
        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken()) - 1;
            int to = Integer.parseInt(st.nextToken()) - 1;
            graph.get(from).add(to);
        }

        Solution(graph);

    }

    public static void Solution(List<List<Integer>> graph) {
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[x] = 0;
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>((left, right) -> {
            return left.get(1) - right.get(1);
        });

        pq.add(List.of(x, distance[x]));

        while (!pq.isEmpty()) {
            List<Integer> idxDist = pq.poll();
            int dist = idxDist.get(1);

            List<Integer> adjust = graph.get(idxDist.get(0));

            for(Integer idx: adjust){
                if(distance[idx] > 1 +dist){
                    distance[idx] = 1+ dist;
                    pq.add(List.of(idx,distance[idx]));
                }
            }
        }
        boolean flag = true;
        for(int i=0; i<n; i++){
            if(distance[i] == k){
                flag = false;
                System.out.println(i+1);
            }
        }
        if(flag) System.out.println("-1");
    }

}
