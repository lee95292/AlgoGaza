package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.TreeMap;

public class J4358 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> statMap = new TreeMap<String,Integer>();

        double total =0;
        while(true){
            String tree = br.readLine();
            if(tree == null) break;
            statMap.put(tree, statMap.getOrDefault(tree, 0) + 1);
            total+=1;
        }

        for(String key: statMap.keySet()){
            System.out.println(key+" "+rount4th(statMap.get(key)/total));
        }
    }

    public static String rount4th(double n){
        return String.format("%.4f", Math.round((n*1000000))/(double)10000); 
    }
    
}
