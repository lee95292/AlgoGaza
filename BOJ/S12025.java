/*
REDO REMIND
12025 장난꾸러기 영훈

!!!!!!!!!!!!재시도 할때 풀이 읽지 말기!!!!!!!!!!!!!!!

문제 설명:
숫자로 이뤄진 비밀번호 중, 1,2를 6,7로 / 6,7을 1,2로 바꾸어놓았을 수 있음
이 때, 비밀번호로 가능한 모든 경우의 수 중, 사전식 정렬했을 때, K번째 비밀번호를 찾기


풀이: 
1/2/6/7이 포함된 인덱스 개수를 세고, K를 2진수로 마스킹해주면 1인 경우, 더 큰 숫자(6,7)로 바꿔주면 정답

주의점:
Math.pow(2,64)의 경우, 부동소수점 이후의 값들은 누락되므로 Java 사용 시 주의 필요
비트마스킹 연산 알아두면 좋을듯..!
*/
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class S12025 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] seq = br.readLine().split("");
        long k = Long.parseLong(br.readLine())-1;
        int m = 0, n = seq.length;
        for(int i=0; i<n; i++){
            String r = seq[i];
            if(isContain(r)) m +=1;
        }
        // System.out.println("tt"+Long.toBinaryString(k));
        // System.out.println(k);
        // System.out.println(pow(2,m));
        if(k >= pow(2,m)){
            System.out.println(-1);
            return;
        }
        int[] mask = new int[m];
        for(int i= 0; i < m; i++){
            if(k > 0){
                mask[m-1-i] = (int)k&1;
                k >>=1;
            }
        }
        int midx = m-1;
        for(int i=n-1; i>=0; i--){
            String r = seq[i];
            if(!isContain(r)) continue;
            if(mask[midx] == 1){
                if( r.equals("1")) seq[i] = "6";
                else if( r.equals("2")) seq[i] = "7";
            }
            if(mask[midx] == 0){
                if( r.equals("6")) seq[i] = "1";
                else if (r.equals("7")) seq[i] = "2";
            }
            midx --;
        }
        StringBuilder sb = new StringBuilder();
        for(String i : seq){
            sb.append(i);
        }
        System.out.println(sb.toString());
        /*
         * 
         * 1. seq에서 1,6,7,2의 개수 m을 센다
         * 2. k를 이진수: 100 
         */
    }
    public static boolean isContain(String x){
        if(x.equals("1") || x.equals("2")|| x.equals("6")|| x.equals("7")) return true;
        return false;
    }

    public static long pow(int a,int b){
        long ret = 1;
        for(int i=0; i<b;i++){
            ret = ret*a;
        }
        return ret;
    }
}



/*
111116111111111111111111111111111111111111111111111111111111
1152921504606846975

 */