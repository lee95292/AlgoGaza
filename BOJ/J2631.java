/*
RETRY: 230602
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J2631 {
    static int n;
    static int[] arr, length;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        length = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        int max = 0;
        for (int i = 0; i < n; i++) {
            length[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    length[i] = Math.max(length[i], length[j] + 1);
                    max = Math.max(max, length[i]);
                }
            }
        }

        // System.out.println(Arrays.toString(length));
        System.out.println(n - max);
    }

    public static void move(int idx, int k) {
    }

}
