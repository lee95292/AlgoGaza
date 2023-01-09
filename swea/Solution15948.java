package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Solution15948 {
    private static int answer;
    private static int[] dx = {0,0,1,-1};
    private static int[] dy = {1,-1,0,0};

    public static void main(String[] args) throws IOException{
        int T;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            answer = 100000;
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c= Integer.parseInt(st.nextToken());
            String map[][] = new String[r][c];
            for(int ri = 0; ri < r; ri++){
                String line = br.readLine();
                for(int ci =0; ci < c; ci++){
                    map[ri][ci] = String.valueOf(line.charAt(ci));
                }
            }
            Map<String,Boolean> used = new HashMap<>();
            used.put(map[0][0],true);
            System.out.println("#"+(i+1)+" "+Solution(0,0,r,c,1,used, map));

        }
    }


    public static int Solution(int ri, int ci, int r, int c,int ans,Map<String,Boolean> used, String[][] map){
        if( ri < 0 || ci < 0 || ri >= r || ci >= c) return ans;
        
        int max = 1;
        for(int i=0 ; i<4 ;i++){
            int rp = ri + dy[i];
            int cp = ci + dx[i];
            if( rp < 0 || cp < 0 || rp >= r || cp >= c) continue;

            if(used.getOrDefault(map[rp][cp], false) == true) continue;
            else used.put(map[rp][cp], true);
            // System.out.println(rp+" "+cp+" "+used+" "+max+" "+ans);
            max = Math.max(Solution(rp, cp, r, c, ans+1, used, map),max);
            used.put(map[rp][cp], false);
            
        }
        return Math.max(ans,max);
    }
    
}




