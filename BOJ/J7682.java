/*
 * RETRY REDO
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class J7682 {
    static int[][] checkList = new int[][]{
        {0,0}, {1,0}, {2,0}, {0,1}, {0,2}
    };
    static int[][] moves = new int[][]{
        {1,0}, {1,1}, {0,1}
    };
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inString = "";
        while(true){
            int cnt[] = new int[2];
            inString = br.readLine();
            if(inString.equals("end")) break;

            Integer[] seq = Arrays.stream( (inString.split(""))).map((a) -> {
                if(a.equals("."))return 0;
                else if(a.equals("O")) return 1;
                return 2;
            }).toArray(Integer[]::new);
            int[][] grid = new int[3][3];
            for(int i=0; i<3; i++){
                for(int j=0; j<3; j++){
                    grid[i][j] = seq[3*i+j];
                    if(seq[3*i+j] >0)cnt[seq[3*i+j]-1]++;
                }
            }
            // System.out.println(Arrays.toString(seq));
            // System.out.println(Arrays.toString(cnt));
            // 
            for(int i=0; i<3;i++){
                System.out.println(Arrays.toString(grid[i]));
            }
            int[] rcnt = check(grid);
            if(cnt[0] +1 == cnt[1] && rcnt[1] == 1 && rcnt[0] == 0){ // 마지막 X
                System.out.println("valid1");
            }
            else if(cnt[0] == cnt[1] && rcnt[0] == 1 && rcnt[1] == 0){ // 마지막 O
                System.out.println("valid2");
            }else if(cnt[1] == 5 &&rcnt[0]+rcnt[1] == 0 && isFull(seq)){
                System.out.println("valid3");
            }else{
                System.out.println("invalid");
            }
        }
    }
    public static boolean isFull(Integer[] seq){
        for(Integer x : seq){
            if(x == 0) return false;
        }
        return true;
    }
    public static int[] check(int[][] grid){
        int[] scnt = new int[2];
        for(int[] pos: checkList){
            Queue<int[]> que = new LinkedList<>(); // [len, O/X, x,y,dir]
            int p = grid[pos[1]][pos[0]];
            que.add(new int[]{0,p, pos[0],pos[1],0});
            que.add(new int[]{0,p, pos[0],pos[1],1});
            que.add(new int[]{0,p, pos[0],pos[1],2});
            boolean flag = false;
            while(que.size() > 0){
                int[] cur = que.poll();
                int len = cur[0], player = cur[1], x=cur[2], y=cur[3], move = cur[4];
                if(len == 2){
                    flag = true;
                    break;
                }
                int cx = x+moves[move][0], cy =y+ moves[move][1];
                if(GRID_OOR(cx, cy)) continue;
                if(grid[cy][cx] != player) continue;
                que.add(new int[]{len+1, player, cx, cy, move});
            }
            if(flag) scnt[p-1]++; 

        }
        return scnt;
    }
    public static boolean GRID_OOR(int x,int y){
        if(0<= x && x< 3 && 0 <= y && y < 3)return false;
        return true;
    }
}
