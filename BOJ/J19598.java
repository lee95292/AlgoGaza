/*
REDO ( last solved: 2023.05.03)
최소 회의실 배정
REDO, 설명 생략
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class J19598 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        List<long[]> sedmap = new LinkedList<>();
        for(int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            long start = Integer.parseInt(st.nextToken());
            long end = Integer.parseInt(st.nextToken());

            sedmap.add(new long[]{i,start,end});
        }
        sedmap.sort((a,b) -> Long.compare(a[1],b[1]));
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> a-b);
        for(long[] info : sedmap){
            if(pq.size() == 0){
                pq.add((int)info[2]);
                continue;
            }
            long mined = pq.peek();
            if(mined <= info[1]){
                pq.poll();
                pq.add((int)info[2]);
            }else{
                pq.add((int)info[2]);
            }
        }   
        System.out.println(pq.size());
    }
    
}
