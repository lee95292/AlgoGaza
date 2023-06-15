package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J25635 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] arr = Arrays.stream(br.readLine().split(" ")).mapToLong(v -> Long.parseLong(v)).toArray();
        if (n == 1) {
            System.out.println(1);
            return;
        }
        Arrays.sort(arr);
        long[] accsum = new long[n];
        accsum[0] = arr[0];

        for (int i = 1; i < n; i++) {
            accsum[i] = arr[i] + accsum[i - 1];
        }
        if (arr[n - 1] > accsum[n - 2] + 1) {
            arr[n - 1] = accsum[n - 2] + 1;
        }
        System.out.println(accsum[n-2]+arr[n-1]);

    }

}
