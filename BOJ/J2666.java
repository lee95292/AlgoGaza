package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J2666 {
    static int n,m;
    static int[] open, closet, query;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        closet = new int[n];
        open = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)-1).toArray();
        // System.out.println(Arrays.toString(open));
        closet[open[0]] = 1;
        closet[open[1]] = 1;
        m = Integer.parseInt(br.readLine());
        query = new int[m];

        for(int i=0; i<m; i++){
            query[i] = Integer.parseInt(br.readLine())-1;
        }
        System.out.println(solve(open[0],open[1],0));
    }

    public static int solve(int l,int r,int c){
        if(c == m) return 0;
        int x = query[c];
        // System.out.println(Arrays.toString(closet));
        // System.out.println(l+" "+r+" "+c+" "+m);
        int lrt = Math.abs(x-l);
        closet[l] = 0;
        closet[x] = 1;
        lrt += solve(x,r,c+1);

        int rrt = Math.abs(x-r);
        closet[l] = 1;
        closet[r] = 0;
        rrt += solve(l,x, c+1);
        // System.out.println(c+"lrt rrt"+lrt+" "+rrt);
        return Math.min(lrt,rrt);

    }
    
}
