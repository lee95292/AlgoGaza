package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class J1034 {
    static int m,n;
    static int[][] grid;
    static int[] toggle;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][m];
        toggle = new int[m];
        for(int i=0; i<n; i++){
            grid[i] = Arrays.stream(br.readLine().split("")).mapToInt(v -> Integer.parseInt(v)).toArray();
            System.out.println(Arrays.toString(grid[i]));
            for(int j=0; j<m; j++){
                if(grid[i][j] ==1 )toggle[j]++;
            }
        }

        int k = Integer.parseInt(br.readLine()) % m;

    }
    public static void solve(){}
}
