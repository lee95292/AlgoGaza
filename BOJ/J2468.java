package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class J2468 {
    static int[][] grid,visit;
    static int n, answer, left=0, right=100;
    static int[] dx = {1,0,0,-1}, dy = { 0,1,-1,0};

    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        grid = new int[n][n];
        visit = new int [n][n];
        answer = 0;
        
        for(int i=0; i<n; i++){
            grid[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(w -> Integer.parseInt(w)).toArray();
        }
        for(int k=0; k<=100; k++){
            int cnt=0;
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    if(visit[i][j] <= k && grid[i][j] > k) {
                        cnt++;
                        bfs(j,i,k);
                    }
                }
            }
            answer = Math.max(answer,cnt);
        }
        System.out.println(answer);
    }
    public static void bfs(int x,int y, int d){
        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{x,y});
        visit[y][x] = d+1;
        while(que.size() > 0){
            int[] fst = que.poll();
            int nx= fst[0], ny= fst[1];
            for(int i=0; i<4; i++){
                int cx = nx + dx[i], cy = ny+ dy[i];
                if(GRID_OOR(cx,cy)) continue;
                if(visit[cy][cx] == d+1) continue;
                if(grid[cy][cx] <= d) continue;
                visit[cy][cx] = d+1;
                que.add(new int[]{cx,cy});
            }
        }
    }
    public static boolean GRID_OOR(int x,int y){
        if(0<=x && x<n && 0<= y && y<n) return false;
        return true;
    }
    
}
