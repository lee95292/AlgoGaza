/*
Parametric Serch, Binary Serch, 이분탐색, 이진탐색
케이크 자르기
케이크를 4개 커팅 포인트에서 자를 때, 가장 작은 조각의 최대 크기
최대크기를 파라미터로 해, 파라매트릭 서치
마지막 조각 고려하기!
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class J17179 {
    static int n,m,cakelen;
    static int[] cutpoint, cutcnt;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m  = Integer.parseInt(st.nextToken());
        cakelen = Integer.parseInt(st.nextToken());

        cutpoint = new int[m];
        cutcnt = new int[n];
        for(int i=0; i<m; i++){
            cutpoint[i] = Integer.parseInt(br.readLine());
        }
        for(int i=0; i<n; i++){
            cutcnt[i] = Integer.parseInt(br.readLine());
            int l = 0;
            int r = 4000000;
            int mid = (l+r)/2;
            int answer = 0;
            while(l<=r){
                mid = (l+r)/2;
                // System.out.println("====");
                // System.out.println(String.format("l,r: %d %d", l,r));
                // System.out.println(String.format("mid,answer: %d %d", mid,answer));
                if(check(mid,cutcnt[i])){
                    answer = mid;
                    l = mid+1;
                }else{
                    r = mid-1;
                }
            }
            System.out.println(answer);
        }

    }
    public static boolean check(int mid, int cnt){
        int cuted = 0;
        int cutcount = 0;
        for(int i=0; i<m ;i++){
            if( cutpoint[i] - cuted >= mid && cakelen - cutpoint[i] >= mid){
                cuted = cutpoint[i];
                cutcount+=1;
            }

            if(cutcount >= cnt) return true;
        }
        return false;
    }
    
}

/*
1 5 70
10
20
35
55
60
5
 */