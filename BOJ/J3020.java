/*
REDO
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class J3020 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int[] up = new int[h];
        int[] down = new int[h];
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine())-1;
            if (i % 2 == 0)
                up[x]++;
            else
                down[h - x -1]++;
        }
        for (int i = h - 2; i >= 0; i--) {
            up[i] += up[i + 1];
        }
        int min = Integer.MAX_VALUE, mincnt = 0;
        for (int i = 1; i < h; i++) {
            down[i] += down[i - 1];
        }
        for (int i = 0; i < h; i++) {
            down[i] += up[i];
            if (min > down[i]) {
                min = down[i];
                mincnt = 1;
            } else if (min == down[i])
                mincnt++;
        }
        
        System.out.println(String.format("%d %d", min, mincnt));
    }
}
