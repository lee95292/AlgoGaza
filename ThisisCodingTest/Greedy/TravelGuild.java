package Greedy;

/*
 * 이것이 코딩테스트다 "그리디 편"
 */
import java.util.*;

class TravelGuild {
    public static void main(String[] args){
        int n = 5;
        int[] traveler = {2,3,1,2,2};
        

        System.out.println("answer="+Solution(n,traveler));
    }

    public static int Solution(int n, int[] traveler){
        Arrays.sort(traveler);

        int idx = 0;
        int answer = 0;
        for(int i =0; i<n; i+=1){
            if(i != idx) continue;
            idx += traveler[i];
            if( idx < n ) answer+=1;
        }
        return answer;
    }
}
