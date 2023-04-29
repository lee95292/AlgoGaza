/*
2615 오목. DFS
1. 대각선 케이스 고려: 우하향, 우상향 (index가 우하향해서 대각선 우상향케이스 체크하지 못한것)
2. 테케 생각하고, 결과 예측하기. 테케 실행결과 납득하지 말기..!
*/
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class J2615 {
    static int[][] borad;
    static int[][][] visit;
    static int[] dx = {1,0,1,1};
    static int[] dy = {0,1,1,-1};
    public static void main (String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        borad = new int[19][19];
        visit = new int[19][19][4];
        for(int i=0; i< 19; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<19;j++){
                borad[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for(int j=0;j<19;j++){
            for(int i=0; i< 19; i++){
                if(borad[i][j] == 0 ) continue;

                if(visit[i][j][0] == 0 &&  travel(j,i,borad[i][j],0) == 5 
                ||(visit[i][j][1] == 0 && travel(j,i,borad[i][j],1)==5) 
                ||(visit[i][j][2] == 0 && travel(j,i,borad[i][j],2) == 5)
                ||(visit[i][j][3] == 0 && travel(j,i,borad[i][j],3) == 5)){
                    System.out.println(borad[i][j]);
                    System.out.println((i+1)+" "+(j+1));
                    return;
                }
            }
        }
        System.out.println(0);

    }
    public static int travel(int x,int y, int color, int direction){
        int cx = x + dx[direction];
        int cy = y + dy[direction];
        visit[y][x][direction]=1;
        // System.out.println("travel("+x+","+y+"),"+direction);
        if (GRID_OOR(cx, cy)) return 1;
        if( borad[cy][cx] != color) return 1;
        return travel(cx, cy, color, direction)+1;
        
    }

    public static boolean GRID_OOR(int x, int y){
        if( (0 <= x && x <19) && (0 <= y && y <19))return false;
        return true;
    }
}