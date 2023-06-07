/*
REDO
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class J1446 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int dist = Integer.parseInt(st.nextToken());
        int[] time = new int[dist+1];//IntStream.range(1,dist+1).toArray();
        int[][] shortroad = new int[n][3];

        for(int i=0; i<n; i++){
            shortroad[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(w -> Integer.parseInt(w)).toArray();
        }

        Arrays.sort(shortroad, (a,b) -> a[1]-b[1]);
        int sidx = 0;
        for(int i=1; i<=dist; i++){
            time[i] = time[i-1]+1;
            while(sidx < n && shortroad[sidx][1] == i){
                time[i] = Math.min(time[i], time[shortroad[sidx][0]] + shortroad[sidx][2]);
                sidx++;
            }
        }
        System.out.println(time[dist]);
    }
}
