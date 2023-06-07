/*
RETRY
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;

public class J1863 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int answer = 0;
        int[] arr= new int[n+1];
        Stack<Integer> stack = new Stack<>();
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int x =Integer.parseInt(st.nextToken());
            arr[i] = Integer.parseInt(st.nextToken());
        }
        for(int i=0 ;i<=n; i++){
            // System.out.println(stack.toString());
            while(stack.size() > 0 && stack.peek() > arr[i]){
                stack.pop();
                answer++;
            }
            if(stack.size() > 0 && stack.peek() == arr[i]) continue;
            stack.push(arr[i]);
        }

        System.out.println(answer);
    }

}

