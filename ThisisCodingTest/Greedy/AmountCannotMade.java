package Greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class AmountCannotMade {
    public static void main(String[] args)throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> moneyList = new ArrayList<>();
        while(st.hasMoreTokens()){
            moneyList.add(Integer.parseInt(st.nextToken()));
        }
        Integer[] money = moneyList.stream().toArray(Integer[]::new);
        System.out.println(Solution(n, money));
    }


    public static int Solution(int n, Integer[] money){
        int answer = 0;
        Arrays.sort(money);

        for(int i=0; i<money.length; i+=1){
            if(money[i]>answer+1) break;
            else answer = answer + money[i];
        }
        answer++;
        return answer;
    }
    /*
    Solution 1. 백준에서 메모리초과 발생: set에 2**1000의 값을 넣게됨.
    public static int Solution(int n, Integer[] money){
        Set<Integer> canMake = new TreeSet<>();
        for(int i=0; i<money.length; i+=1){
            List<Integer> newNums = new ArrayList<>();
            for(Integer num : canMake){
                newNums.add(money[i]+num);
            }
            canMake.addAll(newNums);
            canMake.add(money[i]);
        }
        int answer = 1;

        for(Integer i :  canMake){
            if(i != answer){
                break;
            }
            answer+=1;
        }
        return answer;
    }
     */

}
