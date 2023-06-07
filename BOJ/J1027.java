package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Stack;

public class J1027{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[]  arr = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        int[] answer = new int[n];
        for (int i = 0; i < n-1; i++) {
            answer[i]++;
            answer[i+1]++;
            double slope = arr[i+1] - arr[i];
            for (int j = i+2; j < n; j++) {
                double nextSlope = (double) (arr[j]-arr[i]) / (j - i);
                if (nextSlope > slope) {
                    slope = nextSlope;
                    answer[i]++;
                    answer[j]++;
                }
            }
        }
        int max = Integer.MIN_VALUE;
        for(int i=0 ;i<n; i++){
            max = Math.max(answer[i], max);
        }
        System.out.println(max);
    }
}