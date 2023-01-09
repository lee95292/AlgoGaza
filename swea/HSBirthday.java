package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HSBirthday {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for(int i=0; i<tc; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String n = st.nextToken();
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            System.out.println("#"+i+" "+Solution(n,x,y));
        }
    }

    public static String Solution(String n, int x, int y){
        if(x<y){
            int tmp = y;
            y = x;
            x = tmp;
        }
        StringBuilder answer = new StringBuilder("");

        int idx = n.length();
        while(idx-- >= 0 ){
            
        };

        if(answer=="") return "-1";
        return n;
    }
    
}
