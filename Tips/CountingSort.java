package Tips;

import java.util.Arrays;

public class CountingSort {
    public static void main(String[] args) {
        int n = 7;
        int maxValue = 7;
        int[] array = new int[] { 5, 4, 2, 1, 7, 3, 6 };
        int[] counting = new int[maxValue + 1];
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            counting[array[i]]++;
        }
        for (int i = 1; i <= n; i++) {
            counting[i] += counting[i - 1];
        }
        System.out.println(Arrays.toString(counting));

        for (int i = n - 1; i >= 0; i--) {
            int v = array[i];
            counting[v]--;
            result[counting[v]] = v;
        }
        System.out.println(Arrays.toString(result));
    }
}
