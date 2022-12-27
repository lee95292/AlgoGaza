package Greedy;

import java.util.Arrays;
import java.util.Scanner;

public class Reverse {
    public static void main(String[] args) {
        // String str = "0001100";
        // String str = "11001100110011000001";
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(Solution(str));
        sc.close();
    }

    public static int Solution(String str) {
        Integer[] numbers = Arrays.stream(str.split("")).map(s -> Integer.parseInt(s)).toArray(Integer[]::new);
        int[] count = { 0, 0 };
        Integer prev = -1;
        for(int i=0; i<numbers.length; i+=1){
            if(prev != numbers[i]){
                prev = numbers[i];
                count[prev] +=1;
            }
        }

        return Math.min(count[0], count[1]);
    }
}
