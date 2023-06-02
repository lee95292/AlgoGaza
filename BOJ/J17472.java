package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class J17472 {
    static boolean debug = true;
    static int MAX_DIST = 1000;
    static int n, m, v;
    static int[][] grid;
    static int[] disjset;
    static int[][] moves = new int[][] { { 0, 1 }, { 1, 0 }, { -1, 0 }, { 0, -1 } };
    static List<int[]> edges;
    static int[] rank;

    public static class Pos {
        int x, y;

        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][m];
        for (int i = 0; i < n; i++) {
            grid[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v) * -1).toArray();
        }
        v = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] >= 0)
                    continue;
                Queue<Pos> que = new LinkedList<>();
                que.add(new Pos(j, i));
                grid[i][j] = v;
                while (que.size() > 0) {
                    Pos cur = que.poll();
                    // System.out.println(cur.x + " " + cur.y);
                    for (int[] move : moves) {
                        int cx = cur.x + move[0], cy = cur.y + move[1];
                        if (GRID_OOR(cx, cy))
                            continue;
                        if (grid[cy][cx] != -1)
                            continue;
                        grid[cy][cx] = v;
                        que.add(new Pos(cx, cy));
                    }
                }
                v++;
            }
            if(debug) System.out.println(Arrays.toString(grid[i]));
        }
        int vcnt = v;
        disjset = IntStream.range(0, vcnt).toArray();
        rank = new int[vcnt];
        int[][] wmap = new int[vcnt][vcnt];
        for (int i = 0; i < v; i++) {
            Arrays.fill(wmap[i], MAX_DIST);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0)
                    continue;
                Queue<int[]> que = new LinkedList<>();
                for(int k=0; k<4; k++){
                    // int cx = j + moves[k][0] , cy = i + moves[k][0];
                    // if(GRID_OOR(cx, cy)) continue;
                    que.add(new int[]{j,i,k,0});
                }
                v = grid[i][j];
                while (que.size() > 0) {
                    int[] pop = que.poll();
                    int[] move = moves[pop[2]];
                    int dist = pop[3];
                    int cx = pop[0] + move[0], cy = pop[1] + move[1];

                    if(GRID_OOR(cx, cy)) continue;
                    if(grid[cy][cx] == v)// 같은블록
                        continue;
                    else if(grid[cy][cx] != 0){ // 다른블록
                        if( dist == 1) continue;
                        int arrive =grid[cy][cx];
                        wmap[v][arrive] = Math.min(wmap[v][arrive], dist);
                        wmap[arrive][v] = Math.min(wmap[arrive][v], dist);
                        continue;
                    }
                    que.add(new int[]{cx,cy,pop[2],dist+1});

                }
            }
        }
        if(debug){
            for(int i=0; i<vcnt; i++){
                System.out.println(Arrays.toString(wmap[i]));
            }
        }

        edges = new ArrayList<>();
        for(int i=1; i<vcnt; i++){
            for(int j=1; j<=i; j++){
                if(wmap[i][j] == MAX_DIST) continue;
                if(wmap[i][j] == 1) continue;
                edges.add(new int[]{j,i,wmap[i][j]});
            }
        }
        int answer = 0;
        edges.sort((a,b) -> a[2]-b[2]);
        for(int i=0; i< edges.size(); i++){
            int[] p = edges.get(i);
            int fx = find(p[0]), fy = find(p[1]);
            if( fx == fy) continue;
            union(fx, fy);
            answer += p[2];
        }
        if(debug) System.out.println(Arrays.toString(disjset));
        int check = find(1);
        for(int i=1; i<vcnt; i++){
            if(check != find(i)) {
                System.out.println(-1);
                return;
            }
        }
        if(answer == 0) {
            System.out.println(-1);
            return;
        }
        System.out.println(answer);
    }

    public static boolean GRID_OOR(int x, int y) {
        if (0 <= x && x < m && 0 <= y && y < n)
            return false;
        return true;
    }

    public static void union(int x, int y){
        int fx = find(x), fy = find(y);
        if(fx == fy) return;
        if(rank[fx] > rank[fy])
            disjset[fy] = fx;
        else if(rank[fy] > rank[fx])
            disjset[fx] = fy;
        else{
            disjset[fy] = fx;
            rank[fx]+=1;
        }
            


    }
    public static int find(int x){
        if(disjset[x] == x) return x;
        return find(disjset[x]);
    }

}