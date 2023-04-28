package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
 * 
 * N * N  배열에서, 세로는 증가하는 수열, N번째 큰 수 구하기
 *  Priority Queue로 풀거나 ,직접 구현하기
 */
public class J2075 {
    static int MIN_VALUE = -1000000000;
    public static void main (String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][n];
        int[] maxidxs = new int[n];
        Arrays.fill(maxidxs, n-1);

        for(int i=0;i<n;i++){
            String line = br.readLine();
            StringTokenizer st = new StringTokenizer(line);
            for(int j=0; j<n; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int maxvalue = 0;
        for(int i=0; i<n; i++){
            int idx =-1;
            maxvalue = MIN_VALUE;
            for(int k=0; k<n; k++){
                if(arr[maxidxs[k]][k] > maxvalue){
                    maxvalue = arr[maxidxs[k]][k];
                    idx = k;
                }
            }
            maxidxs[idx] -=1;
        }

        System.out.println(maxvalue);

    }
    
}
