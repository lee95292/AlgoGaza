package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class J20924 {
    static int[][] edges;
    static int root, n;
    static List<List<int[]>> tree;
    static List<List<int[]>> dtree;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        root = Integer.parseInt(st.nextToken());
        tree = new ArrayList<>();
        dtree = new ArrayList<>();
        for(int i=0; i<=n; i++){
            tree.add(new ArrayList<>());
            dtree.add(new ArrayList<>());
        }
        for(int i=0; i<n-1; i++){
            int[] x = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
            tree.get(x[0]).add(new int[]{x[1],x[2]});
            tree.get(x[1]).add(new int[]{x[0],x[2]});
        }
        makeTree(root, -1);
        int giga = root, gigalen = 0;
        for(int i=0; i<n; i++){
            if(dtree.get(giga).size() == 0) break;
            int[] child = dtree.get(giga).get(0);
            if(dtree.get(giga).size() != 1) break;
            giga = child[0];
            gigalen += child[1];
        }
        System.out.println(String.format("%d %d",gigalen,maxdfs(giga)));

    }
    public static void makeTree(int cur, int parent){
        List<int[]> child = tree.get(cur);
        for(int[] edge : child){
            if(edge[0] == parent) continue;
            dtree.get(cur).add(edge);
            makeTree(edge[0], cur);
        }
    }

    public static int maxdfs(int cur){
        List<int[]> child = dtree.get(cur);
        if(child.size() == 0 ) return 0;
        int ret = 0;
        for(int[] edge : child){
            ret = Math.max(ret, edge[1] + maxdfs(edge[0]));
        }
        return ret;
    }


    
}
