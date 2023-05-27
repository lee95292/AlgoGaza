package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class J1976 {
    static int n,m;
    static int[] distset;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        distset = IntStream.range(0,n).toArray();
        
        for(int i=0; i<n; i++){
            int[] x  = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
            for(int j=0; j<n; j++){
                if(x[j] == 1){
                    union(i,j);
                }
            }
        }
        if(m==0){
            System.out.println("NO");
            return;
        }
        int[] x  = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        int root = find(x[0]-1);

        for(int k : x){
            if(find(k-1) != root){
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
    public static int find(int x){
        if(distset[x] == x) return x;
        return find(distset[x]);
    }
    public static void union(int x, int y){
        int fx = find(x), fy = find(y);
        if (fx == fy) return;
        if(fx > fy) distset[fy] = fx;
        else distset[fx] = fy;
        
    }
}
