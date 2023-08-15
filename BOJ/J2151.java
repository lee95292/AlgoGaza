package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class J2151 {
    static int[] dx = new int[] { 1, 0, -1, 0 };
    static int[] dy = new int[] { 0, 1, 0, -1 };
    static int n;

    public static int mirror(int d) {
        if (d == 0)
            return 3;
        if (d == 1)
            return 2;
        if (d == 2)
            return 1;
        if (d == 3)
            return 0;
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[][] grid = new int[n][n];
        int stx = 0, sty = 0;
        int answer =0;
        for (int i = 0; i < n; i++) {
            String[] arr = br.readLine().split("");
            for (int j = 0; j < n; j++) {
                if (arr[j].equals("*"))
                    grid[i][j] = -1;
                else if (arr[j].equals("!"))
                    grid[i][j] = 1;
                else if (arr[j].equals("#")) {
                    grid[i][j] = 2;
                    stx = j;
                    sty = i;
                }
            }
        }

        Queue<int[]> que = new LinkedList<>();
        for (int i = 0; i < 4; i++) {
            // x,y,direction, mirror cnt
            que.add(new int[] { stx, sty, i, 0 });
        }

        while (que.size() > 0) {
            int[] out = que.poll();
            int x = out[0], y = out[1], dir = out[2], mcnt = out[3];

            int cx = x + dx[dir], cy = y + dy[dir];
            if (GRID_OOR(cx, cy))
                continue;
            if (grid[cy][cx] == -1)
                continue;
            if (grid[cy][cx] == 2) {
                if(answer != 0)answer = Math.min(answer, mcnt);
                else answer = mcnt;
                continue;
            }
            if (grid[cy][cx] == 1) {
                que.add(new int[]{cx,cy,mirror(dir),mcnt++});
            }
            que.add(new int[] { cx, cy, dir, mcnt });
        }
        System.out.println(answer);
    }

    public static boolean GRID_OOR(int x, int y) {
        if (0 <= x && x < n && 0 <= y && y < n)
            return false;
        return true;
    }
}
