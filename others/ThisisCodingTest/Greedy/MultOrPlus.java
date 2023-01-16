package Greedy;

/*
 * 이것이 코딩테스트다 "그리디 편"
 */

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class MultOrPlus {
    public static void main(String[] args) {
        String number = "02984";
        System.out.println(Solution(number));
    }

    public static int Solution(String number) {
        int answer = 0;
        List<Integer> numberArray = Arrays.stream(number.split(""))
                .map(num -> Integer.parseInt(num))
                .collect(Collectors.toList());

        for(Integer point : numberArray){
            if(point <2 || answer == 0) answer+= point;
            else answer *= point;
        }
        return answer;
    }

}
