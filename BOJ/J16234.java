package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class J16234 {
    static int[] dx = new int[] { 1, 0, -1, 0 };
    static int[] dy = new int[] { 0, 1, 0, -1 };

    public static class Pos {
        int x, y;

        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int[][] grid = new int[n][n];
        int[][] visit;

        int answer = 0;
        for (int i = 0; i < n; i++) {
            grid[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        }
        while (true) {
            visit = new int[n][n];
            int[] visitCnt = new int[n * n + 1];
            int[] connectSum = new int[n * n + 1];
            int visitNum = 1;
            boolean moved = false;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visitNum == visit[i][j])
                        continue;
                    Queue<Pos> que = new LinkedList<>();
                    que.add(new Pos(j, i));
                    visit[i][j] = visitNum;
                    while (que.size() > 0) {
                        Pos cur = que.poll();
                        connectSum[visitNum] += grid[cur.y][cur.x];
                        visitCnt[visitNum]++;
                        for (int d = 0; d < 4; d++) {
                            int nx = cur.x + dx[d], ny = cur.y + dy[d];
                            if (GRID_OOR(nx, ny))
                                continue;
                            if (visit[ny][nx] == visitNum)
                                continue;
                            int diff = Math.abs(grid[ny][nx] - grid[cur.y][cur.x]);
                            if (l > diff || diff > r)
                                continue;
                            que.add(new Pos(nx, ny));
                            visit[ny][nx] = visitNum;
                            if (!moved)
                                moved = true;
                        }
                    }
                    visitNum++;
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int vflag = visit[i][j];
                    if (vflag == 0)
                        continue;
                    grid[i][j] = connectSum[vflag] / visitCnt[vflag];
                }
            }

            if (!moved)
                break;
            else
                answer++;

        }
        System.out.println(answer);
    }

    public static boolean GRID_OOR(int x, int y) {
        if (0 <= x && x < n && 0 <= y && y < n)
            return false;
        return true;
    }
}
