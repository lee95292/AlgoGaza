/*
 * 
 * 1430 공격.
 * 1. 적: 0, 포탑; 1~ , 거리 내에 있으면 1, 아니면 0
 * 2. BFS를 통해 적부터 도달가능한 포탑 찾기. 왜 다익스트라, 플로이드 와샬 안될까? 
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class J1430 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int MAX_VAL = 51;
        double answer = 0;
        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int mx = Integer.parseInt(st.nextToken());
        int my = Integer.parseInt(st.nextToken());
        int[][] dist = new int[n + 1][2];
        int[][] distmap = new int[n + 1][n + 1];
        double[] divmap = new double[n + 1];
        divmap[1] = (double) d;
        for (int i = 2; i <= n; i++) {
            divmap[i] = divmap[i - 1] / 2;
        }
        for (int i = 0; i <= n; i++) {
            Arrays.fill(distmap[i], MAX_VAL);
        }
        dist[0][0] = mx;
        dist[0][1] = my;
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int tx = Integer.parseInt(st.nextToken());
            int ty = Integer.parseInt(st.nextToken());
            dist[i][0] = tx;
            dist[i][1] = ty;
        }

        for (int i = 0; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                double ijdist = getDist(dist[i][0], dist[i][1], dist[j][0], dist[j][1]);
                if (ijdist <= r) {
                    distmap[i][j] = 1;
                    distmap[j][i] = 1;
                }
            }
        }
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                for (int k = 0; k <= n; k++) {
                    distmap[i][j] = Math.min(distmap[i][j], distmap[i][k] + distmap[k][j]);
                    distmap[j][i] = distmap[i][j];
                }
            }
        }
        Queue<int[]> que = new LinkedList<>();
        que.offer(new int[]{0,0});
        int[] visit = new int[n+1];
        while(que.size() >0 ){
            int[] qv = que.poll();
            int idx = qv[0];
            int level = qv[1];
            if(level>0) answer += (double)d /Math.pow(2,level-1);
            for(int i=1; i<=n;i++){
                if(distmap[idx][i] == 1 && visit[i]==0) {
                    visit[i] = 1;
                    que.offer(new int[]{i,level+1});
                }
            }
        }
        System.out.println((answer * 100) / 100);
    }

    public static double getDist(int x1, int y1, int x2, int y2) {
        int x = x1 - x2;
        int y = y1 - y2;
        return Math.sqrt(x * x + y * y);
    }
}


/*
 * 
9 1 4 0 2
1 2
2 2
3 2
4 2
5 2
3 0
3 1
3 3
3 5

30 2 3 0 0
1 0
3 0
5 0
7 0
9 0
11 0
13 0
15 0
17 0
19 0
21 0
23 0
25 0
27 0
29 0
 */