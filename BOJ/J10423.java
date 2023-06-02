/*
MST, 최소스패닝 트리
 */
package BOJ;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;

public class J10423 {
    static int[] nmk, roots, dijset;
    static Map<Integer, Boolean> isRoot;
    static int n, m, k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        nmk = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        roots = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        isRoot = new HashMap<>();
        n = nmk[0];
        m = nmk[1];
        k = nmk[2];
        dijset = IntStream.range(0, n+1).toArray();

        // for (int root : roots) {
        //     isRoot.put(root, true);
        // }
        int cnt = k;
        for(int i=0; i<k-1; i++){
            union(roots[i], roots[i+1]);
        }
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        }
        Arrays.sort(edges, (a, b) ->  a[2] - b[2]);
        int answer = 0;
        for(int i=0; i<m; i++){
            int fx = find(edges[i][0]), fy =find(edges[i][1]);
            if(fy!= fx){ //연결되지 않고, !(둘 다 루트)
                union(fx,fy);
                answer += edges[i][2];
                cnt++;
            }
            if(cnt == n) break;
        }
        bw.write(answer);
        bw.flush();
    }
    public static void union(int x,int y){
        int fx = find(x), fy = find(y);
        if(fx == fy) return;
        if( isRoot.getOrDefault(x, false)){
            dijset[fy] = fx;
        }else{
            dijset[fx] = fy;
        }
    }

    public static int find(int x){
        if( x == dijset[x]){
            return x;
        }
        return find(dijset[x]);
    }

}
