/*
 * BOJ.kr/ 27375 금공강 사수, 완탐
 * 평범한 완탐 문제. timeTable[week][time]: 이미 수업이 있는 시간이면 1
 * time범위를 넣을 수 있는지 확인한 후 데이터를 변경해야 함. Atomic하게
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class J27375 {
    static int n,k;
    static int[][] timeTable;
    static int[][] cand; // 요일,시간
    static int answer;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        cand = new int[n][3];
        timeTable = new int[6][11];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            
            cand[i][0] = Integer.parseInt(st.nextToken());
            cand[i][1] = Integer.parseInt(st.nextToken());
            cand[i][2] = Integer.parseInt(st.nextToken());
        }
        
        solve(0,0);
        System.out.println(answer);
    }
    
    public static void solve(int idx, int h){
        if(idx == n){
            // System.out.println(idx+" "+h);
            if(h==k)answer +=1;
            return;
        }
        solve(idx+1, h);
        
        int week = cand[idx][0];
        int st = cand[idx][1];
        int ed = cand[idx][2];

        if(week == 5) return;
        boolean flag = true;
        for(int i=st; i<=ed; i++){
            if(timeTable[week][i] == 1) flag = false;
        }
        if(!flag) return;
        for(int i=st; i<=ed; i++){
            timeTable[week][i] = 1;
        }
        solve(idx+1, h+ed-st+1);

        for(int i=st; i<=ed; i++){
            timeTable[week][i] = 0;
        }
        return;
    }
}
