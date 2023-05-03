/*
예산, Parametric Search, Binary Search, 이분탐색, 이진탐색
한정 에산을 모두 안전하게 나눠줄 수 있는 상한선 구하기
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class J2512 {
    static int n, maxbudgit;
    static int[] cities;

    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        cities = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int ma = 0;
        for(int i=0;i<n;i++){
            cities[i] = Integer.parseInt(st.nextToken());
            ma = Math.max(ma,cities[i]);
        }
        maxbudgit = Integer.parseInt(br.readLine());
        
        int l = 0;
        int r  =1000000000;
        int mid=(l+r)/2;
        int answer = 0;
        while(l <= r){
            mid = (l+r)/2;
            // System.out.println(" ====");
            // System.out.println(l+" "+r);
            // System.out.println(answer+" "+mid);
            if(check(mid)){
                answer = mid;
                l = mid+1;
            }else{
                r = mid-1;
            }
        }
        // System.out.println(l);
        System.out.println(Math.min(answer,ma));
    }
    public static boolean check(int mid){
        int tot = 0;
        for(int i=0; i<n; i++){
            tot+=Math.min(mid, cities[i]);
            if(tot > maxbudgit) return false;
        }
        return true;
    }
    
}
