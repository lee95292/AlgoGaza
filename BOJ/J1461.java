/*
 * REDO
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class J1461 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        int[] books = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        List<Integer> neg = new ArrayList<>();
        List<Integer> pos = new ArrayList<>();
        for(int b : books){
            if(b > 0) pos.add(b);
            else neg.add(b);
        }

        neg.sort((a,b) -> a-b);
        pos.sort((a,b) -> b-a);
        int nidx = 0, pidx = 0;
        int answer = 0;
        while(nidx < neg.size()){
            answer+= neg.get(nidx)*-1*2;
            nidx+=m;
        }
        while(pidx < pos.size()){
            answer += pos.get(pidx)*2;
            pidx +=m;
        }
        int max = 0;
        if(neg.size() > 0) max = Math.max(max, neg.get(0)*-1);
        if(pos.size() > 0) max = Math.max(max, pos.get(0));
        answer -= max;
        System.out.println(answer);
    }
    
}
