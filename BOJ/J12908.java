package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class J12908 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[][] moves = {
            {1,0},
            {0,1},
            {-1,0},
            {0,-1}
        };
        int sx,sy,ex,ey;
        sx = Integer.parseInt(st.nextToken());
        sy = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        ex = Integer.parseInt(st.nextToken());
        ey = Integer.parseInt(st.nextToken());
        HashMap<int[], int[]> tps = new HashMap<>();
        HashMap<int[], Boolean> visit = new HashMap<>();
        for(int i=0; i<3; i++){
            st = new StringTokenizer(br.readLine());
        
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            tps.put(new int[]{x1,y1}, new int[]{x2,y2});
            tps.put(new int[]{x2,y2}, new int[]{x1,y1});
        }

        PriorityQueue<int[]> que = new PriorityQueue<>((a,b) ->  a[0]-b[0]);
        que.add(new int[]{0,sx,sy});
        visit.put(new int[]{sx,sy}, true);
        while(que.size() > 0){
            int[] p = que.poll();
            System.out.println(Arrays.toString(p)+visit.size());
            visit.put(new int[]{p[1],p[2]},true);
            if(p[1] == ex && p[2] == ey){
                System.out.println(p[0]);
                return;
            }
            for(int[] move: moves){
                int cx = p[1] + move[0];
                int cy = p[2] + move[1];
                if(visit.getOrDefault(new int[]{cx,cy}, false)) continue;
                for(int[] tp: tps.keySet()){
                    if(cx == tp[0] && cy == tp[1]){
                        int[] v = tps.get(tp);
                        int[] x= new int[]{p[0]+10, v[0], v[1]};
                        que.add(x);
                        visit.put(new int[]{v[0],v[1]}, true);
                    }
                }
                int[] x =  new int[]{p[0]+1, cx,cy};
                que.add(new int[]{p[0]+1, cx,cy});
            }
        }

    }
    
}
