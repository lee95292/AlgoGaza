package coding_test.naverfin;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class F {
    public static void main(String[] args){
        List<Integer> asd =new ArrayList<>();
        Set<Integer> a =new HashSet<>();
        Math.max(0, 0)
    }
    
    public int[] Solution(int[] periods, int[][] payments, int[] estimates){
        int n = periods.length;
        int[] answer = new int[2];
        for(int i=0; i<n; i+=1){
            int nowSum = Arrays.stream(payments[i]).sum();
            boolean nowVip = isVip(nowSum, periods[i]);
            boolean nextVip = isVip(nowSum-payments[i][0]+estimates[i], periods[i]+1);

            if(nowVip == false && nextVip == true) answer[0] +=1;
            if(nowVip == true  && nextVip == false) answer[1] +=1;
        }
        return answer;
    }
    public boolean isVip(int paySum, int period){
        if(period >= 24 && paySum >= 900000) return true;
        else if(period >= 60 && paySum >= 600000) return true;

        return false;
    }
}
