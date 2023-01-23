package others.softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

/*
슈퍼컴퓨터 클러스터!
이진탐색..외우자
while(left <= right){
    mid = (left + right) /2;
    if(check){
        low = mid+1;
        answer = low;
    }else{
        high = mid-1;
    }
}
 */
public class S1204 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long[] p = new long[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int performance = Integer.parseInt(st.nextToken());
            p[i] = performance;
        }
        
        System.out.println(Solution(n, b, p));
    }

    public static long Solution(int n, long b, long[] p) {
        Arrays.sort(p);
        long low = p[0];
        long high = p[n - 1] + (long) Math.sqrt(b);
        long mid;
        long answer = 0;

        while (low <= high) {
            mid = (high + low) / 2;
            if (check(mid, p, b)) {
                low = mid + 1;
                answer = mid;
            } else
                high = mid - 1;
        }
        for (int i = 0; i < n; i++) {
            long dif = low - p[i];
            if (dif > 0) {
                p[i] += dif;
                b -= dif * dif;
            }
        }
        return answer;
    }

    public static boolean check(long val, long[] p, long b) {
        for (long performance : p) {
            if (performance < val)
                b -= (val - performance) * (val - performance);
            if (b < 0)
                return false;
        }
        return true;
    }

}