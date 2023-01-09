package BOJ;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

// 1715 카드 정렬하기
class Solution1715 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        for (int i = 0; i < n; i += 1) {
            numbers[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(numbers);
        System.out.println(Solution(n,numbers));

    }

    public static int Solution(int n, int[] numbers){
        if(n == 1 ) return 0;
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int number: numbers){
            pq.add(number);
        }
        
        while(pq.size() > 1){
            int a1 = pq.poll();
            int a2 =pq.poll();
            answer += a1+a2;
            pq.add(a1+a2);
        }
        
        return answer;
    }
}
 