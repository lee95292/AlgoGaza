package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;
public class J1647{
    static int[][] edges;
    static int[] dist;
    public static void main(String[] args) throws IOException{
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        edges = new int[m][3];
        dist = IntStream.range(0,n+1).toArray();
        for(int i=0; i<m; i++){
            edges[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        }
        Arrays.sort(edges, (a,b) -> a[2]-b[2]);
        int answer = 0;
        int last = 0;
        for(int i=0; i<m; i++){
            int x = edges[i][0], y = edges[i][1];
            int fx = find(x), fy = find(y);
            if(fx == fy) continue;
            union(fx,fy);
            answer += edges[i][2];
            last = edges[i][2];
        }
        System.out.println(answer-last);
    }
    public static int find(int x){
        if(x == dist[x]) return x;
        return find(dist[x]);
    }
    public static void union(int x, int y){
        int fx = find(x), fy = find(y);
        if(fx == fy) return;
        if(fx > fy) dist[fx] = fy;
        else dist[fy] = fx;
    }
}