package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class S1890 {
    static class Pair{
        int x,y;
        Pair(int x,int y){
            this.x = x;
            this.y = y;
        }
    }
    static int n;
    static int[][] grid;
    static long[][] answer;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        grid = new int[n][n];
        answer = new long[n][n];
        for(int i=0; i<n; i++){
            grid[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        }
        answer[0][0] =1;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                int nx = j + grid[i][j], ny = i + grid[i][j];
                if(i == n-1 && j == n-1) break;
                if(!GRID_OOR(nx,i)){
                    answer[i][nx] += answer[i][j];
                    // System.out.println(nx+" "+i+" "+answer[i][nx]);
                }
                if(!GRID_OOR(j,ny)){
                    answer[ny][j] += answer[i][j];
                    // System.out.println(j +" "+ny+" "+answer[ny][j]);
                }
            }
        }
        for(int i=0; i<n; i++){
            System.out.println(Arrays.toString(answer[i]));
        }
        System.out.println(answer[n-1][n-1]);
    }

    public static boolean GRID_OOR(int x,int y){
        if(0 <= x && x < n && 0<= y && y < n)return false;
        return true;
    }
}
