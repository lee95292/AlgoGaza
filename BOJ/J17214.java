/*
문자열 파싱해서 적분하는 문제
REMIND:
1. 수식 게산으로 나올 때 고려할것들
-10, 0 , 큰수 등

2. Java에서 문자열 숫자인지 체크
Character.isDigit(char x)
Integer.parseint with try-catch
 */
package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class J17214 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> var = new ArrayList<>();
        String inpt = br.readLine();
        StringBuilder token = new StringBuilder();
        for (int i = 0; i < inpt.length(); i++) {
            char k = inpt.charAt(i);
            if ((k == '+' || k == '-')) {
                if (token.length() > 0) {
                    var.add(token.toString());
                    token = new StringBuilder();
                }
                var.add(String.valueOf(k));
                continue;
            }
            token.append(k);
        }
        var.add(token.toString());
        // System.out.println(var.toString());
        if(var.get(0).equals("0")){
            System.out.println("W");
            return;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < var.size(); i++) {
            sb.append(integral(var.get(i)));
        }
        sb.append("+W");

        System.out.println(sb.toString());
    }

    public static String integral(String s) {
        if (s.equals("+") || s.equals("-"))
            return s;
        StringBuilder st = new StringBuilder("x");
        StringBuilder it = new StringBuilder();
        int cnt = 1;
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.codePointAt(i)))
                it.append(s.charAt(i));
            else {
                st.append(s.charAt(i));
                cnt++;
            }
        }
        String ret = st.toString();
        if(it.length() > 0){
            Integer num = Integer.parseInt(it.toString()) / cnt;
            if(num > 1)ret = num.toString() + st.toString();

        }

        return ret;
    }
}
