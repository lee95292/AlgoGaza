package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class J20437 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for(int t=0; t<tc; t++){
            String s = br.readLine();
            int k = Integer.parseInt(br.readLine());
            Map<Character, List<Integer>> codeMap = new HashMap<>();
            for(char a = 'a'; a <='z'; a++){
                codeMap.put(a, new ArrayList<>());
            }
            int std = 0;
            for(int i=0; i<s.length(); i++){
                codeMap.get(s.charAt(i)).add(i);
                std = Math.max(codeMap.get(s.charAt(i)).size(), std);
            }
            if(std < k){
                System.out.println(-1);
                continue;
            }
            int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
            for(char a = 'a';a<='z';a++){
                List<Integer> idxs = codeMap.get(a);
                if(idxs.size() <k ) continue;
                for(int i=k-1; i<idxs.size(); i++){
                    int st = i-k+1, stval = idxs.get(i-k+1);
                    int ed = i, edval = idxs.get(i);
                    int len = edval - stval + 1;
                    if(min > len) min = len;
                    if(max < len) max = len;
                }
            }
            System.out.println(min+" "+max);
            // System.out.println(codeMap.toString());
        }
    }
}
