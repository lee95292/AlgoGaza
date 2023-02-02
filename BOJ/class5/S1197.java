/*
 * 백준 클래스5 최소스패닝트리: MST, union-find
 */
package BOJ.class5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class S1197 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int[] unionSet = new int[v];
        for(int i=0; i<v;i ++){
            unionSet[i] = i;
        }
        
        List<int[]> rs = new ArrayList<>();
        for(int i=0; i<e; i++){
            st = new StringTokenizer(br.readLine());
            int fr = Integer.parseInt(st.nextToken())-1;
            int to = Integer.parseInt(st.nextToken())-1;
            int we = Integer.parseInt(st.nextToken());
            rs.add(new int[]{fr,to,we});
        }
        rs.sort((l,r) -> l[2] - r[2]);
        int answer= 0;
        for(int[] edge : rs){
            if(!union(unionSet, edge[0], edge[1])){
                answer += edge[2];
            }
        }
        System.out.println(answer);
    }
    public static int find(int[] uset, int x){
        if(uset[x] == x){
            return x;
        }

        return find(uset, uset[x]);
    }

    public static boolean union(int[] uset,int x,int y){
        int xr = find(uset, x);
        int yr = find(uset, y);
        if(xr == yr) return true;
        if(xr > yr){
            uset[yr] = xr;
            return false;
        }else{
            uset[xr] = yr;
            return false;
        }
    }
}
