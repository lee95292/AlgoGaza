package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class J1021 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] list = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        LinkedList<Integer> que = new LinkedList<>();
        for(int i=0; i<n;i++){
            que.offer(i+1);
        }
        int answer = 0 ;
        // System.out.println("asdad"+que.toString());
        for(int x : list){
            // System.out.println("st  "+que.toString()+" "+x);
            int cnt = 0;
            while(x != que.get(cnt) && x != que.get(que.size()-cnt-1))
                cnt++;
            

            answer += cnt;
            if(cnt >0 && que.get(cnt) == x){
                while(cnt-- >0){
                    int add= que.pollFirst();
                    que.offerLast(add);
                }
            }else if(cnt >=0 && que.get(que.size()-1-cnt) == x){
                if(que.size()>1)answer++;
                while(cnt-- >=0){
                    int add =que.pollLast();
                    que.offerFirst(add);
                }
            }
            // System.out.println(que.toString()+" "+x);
            // System.out.println(answer);
            que.remove(0);
        }
        System.out.println(answer);
    }
    
}
