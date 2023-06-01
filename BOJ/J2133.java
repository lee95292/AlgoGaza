package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class J2133 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        if(n%2==1){
            System.out.println(0);
            return;
        }
        long answer=0;
        for(int i=0; i<n/2; i++){
            long r= pow(3,n/2-i*2) * combination(n/2-1,i) *2;
            System.out.println(r);
            answer += pow(3,n/2-i*2) * combination(n/2-1,i) *2;//* pow(3, n/2-1-i);
        }
        System.out.println(answer);

    }
    public static long combination(int n, int r){
        if(n == 0) return 1;
        long ret =  1;
        int l = Math.max(r, n-r), pl = Math.min(r,n-r);
        for(int i=l+1; i<=n; i++){
            ret*=i;
            while(pl > 0 && ret % pl == 0){
                ret/=pl;
                pl--;
            }
        }
        return ret;
    }
    public static long pow(int x, int y){
        long ret = 1;
        for(int i=0; i<y;i++){
            ret*=x;
        }
        return ret;
    }
    
}
