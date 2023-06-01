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

    static int[][] moves = new int[][]{
        {1,0},{0,1},{1,1},{-1,-1},{1,-1},{-1,1},{-1,0},{0,-1}
    };
    static int[][][] checkList = new int[][][]{
        {{0,0},{1,0},{2,0}}, {{0,1},{1,1},{2,1}}, {{0,2},{1,2},{2,2}},
        {{0,0},{0,1},{0,2}}, {{1,0},{1,1},{1,2}}, {{2,0},{2,1},{2,2}},
        {{0,0},{1,1},{2,2}}, {{2,0},{1,1},{0,2}},
        
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
            int[] rcnt = check(grid);
            // for(int i=0; i<3;i++){
            //     System.out.println(Arrays.toString(grid[i]));
            // }
            // System.out.println(Arrays.toString(rcnt));
            // System.out.println("======");
            if(cnt[1] > 5 || cnt[0] > 4) System.out.println("invalid");
            else if(cnt[0] +1 == cnt[1] && rcnt[1] == 1 && rcnt[0] == 0){ // 마지막 X
                System.out.println("valid");
            }
            else if(cnt[0] == cnt[1] && rcnt[0] == 1 && rcnt[1] == 0){ // 마지막 O
                System.out.println("valid");
            }else if(cnt[1] == 5 && cnt[0]==4 && rcnt[0]+rcnt[1] == 0){
                System.out.println("valid");
            }else{
                System.out.println("invalid");
            }
        }
    }

    public static int[] check(int[][] grid){
        int[] scnt = new int[2];
        int[][] visit = new int[9][2];
        for(int i=0; i<9; i++){
            int gx = i%3, gy=i/3;
            Queue<int[]> que = new LinkedList<>(); // [len, O/X, x,y,dir]
            int p = grid[gy][gx];
            if(p == 0 ||visit[gy*3+gx][p-1] > 0) continue;
            que.add(new int[]{0,p, gx,gy});
            boolean flag = false;
            while(que.size() > 0){
                int[] cur = que.poll();
                int len = cur[0], player = cur[1], x=cur[2], y=cur[3];
                visit[y*3+x][player-1] = i+1;
                for(int[] mv : moves){
                    int cx = x+mv[0], cy =y+ mv[1];
                    if(GRID_OOR(cx, cy)) continue;
                    if(grid[cy][cx] != player) continue;
                    if(visit[cy*3+cx][player-1] == i+1 ) continue;
                    que.add(new int[]{len+1, player, cx, cy});
                }
            }
            int k = bingo(visit,p,i+1);
            scnt[p-1] += k;

        }
        return scnt;
    }
    public static int bingo(int[][] visit, int player, int visitch){
        int ret = 0;
        for(int[][] npos : checkList){
            boolean flag = true;
            for(int[] pos : npos){
                if(visit[pos[1]*3+pos[0]][player-1]== visitch) continue;
                flag = false;
                break;
            }
            if(flag) ret +=1;
        }
        if(ret >= 2) return 1;
        return ret;
    }
    public static boolean GRID_OOR(int x,int y){
        if(0<= x && x< 3 && 0 <= y && y < 3)return false;
        return true;
    }
}

/*

XXXOO.XXX
XOXOXOXOX
OXOXOXOXO
XXOOOXXOX
XO.OX...X
.XXX.XOOO
X.OO..X..
OOXXXOOXO
XXXXOOXOO
OOXXXXXOO
XXXOOOXXX
XOXOXOXO.
XXXOOO...
XO.X.OXO.
OO.O.XXXX
XXOXOOXOX
end

 */