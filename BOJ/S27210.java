package  BOJ;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S27210{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        int[] lside = new int[n];
        int[] rside = new int[n];
        st= new StringTokenizer(br.readLine());
        if(st.nextElement().equals("1"))
            lside[0] = 1;
        else
            rside[0] = 1;
        
        for(int i=1; i<n; i++){
            if(st.nextElement().equals("1")){
                lside[i] = lside[i-1]+1;
                rside[i] = Math.max(0,rside[i-1]-1);
            }else{
                rside[i] = rside[i-1]+1;
                lside[i] = Math.max(lside[i-1]-1,0);
            }
        }
        int max = 0;

        for(int i=0; i<n; i++){
            max = Math.max(lside[i],max);
            max = Math.max(rside[i],max);
        }

        System.out.println(max);
    }

}