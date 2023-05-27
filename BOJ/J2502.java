package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class J2502 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int d = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);
        
        int day = 3;
        int pa = 0, ppa = 1;
        int pb = 1, ppb = 0;
        for(int i=0; i<d-2; i++){
            int tmp = pa;
            pa = ppa + pa;
            ppa = tmp;

            tmp = pb;
            pb = ppb + pb;
            ppb = tmp;
            // System.out.println(pa+" "+pb);
        }

        for(int i=1; i<=k/pa; i++){
            for(int j=1;j<=k/pb;j++){
                if(k == i*pa + j * pb){
                    System.out.println(i);
                    System.out.println(j);
                    return;
                }
            }
        }
    }
    
}
