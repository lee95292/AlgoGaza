package BOJ;

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class J1926 {
    public static class Pos {
        int x, y;

        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n, m, cnt, maxsz;
    static int[][] visit, grid;
    static int[][] moves = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][m];
        visit = new int[n][m];

        for (int i = 0; i < n; i++) {
            grid[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            // System.out.println(Arrays.toString(grid[i]));
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visit[i][j] == 1)
                    continue;
                if (grid[i][j] == 0)
                    continue;
                int sz = bfs(j, i);
                cnt++;
                maxsz = Math.max(maxsz, sz);
            }
        }
        System.out.println(cnt);
        System.out.println(maxsz);
    }

    public static int bfs(int sx, int sy) {
        Queue<Pos> que = new LinkedList<>();
        que.add(new Pos(sx, sy));
        visit[sy][sx] =1;
        int size = 1;
        while (que.size() > 0) {
            Pos p = que.poll();
            for (int[] move : moves) {
                int cx = p.x + move[0];
                int cy = p.y + move[1];
                if (GRID_OOR(cx, cy))
                continue;
                if (visit[cy][cx] == 1)
                continue;
                if (grid[cy][cx] == 0)
                continue;
                
                que.add(new Pos(cx, cy));
                visit[cy][cx] =1;
                size++;
            }
        }
        return size;
    }

    public static boolean GRID_OOR(int x, int y) {
        if (0 <= x && x < m && 0 <= y && y < n)
            return false;
        return true;
    }

}
