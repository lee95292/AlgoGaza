package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class HSBirthday {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for(int i=0; i<tc; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String n = st.nextToken();
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            System.out.println("#"+(i+1)+" "+Solution2(n,x,y));
        }
    }

    public static String Solution2(String n, int x, int y){
        if(y>x){
            int tmp = y;
            y = x;
            x = tmp;
        }
        int[] answerList = new int[n.length()];
        Arrays.fill(answerList, x);
        int ridx = -1;
        int next = 0;
        for(int i=0; i<n.length(); i++){
            int value = Character.getNumericValue(n.charAt(i));
            if(value > x) {
                answerList[i] = x;
                break;
            }
            else if(value ==x )continue;
            else if(value > y){
                answerList[i] = y;
                break;
            }
            else if(value == y ){
                answerList[i] = y;
            }
            else {
                answerList[i] = x;
                if(i==0)answerList[i] = 0;
                ridx = i-1;
                next = 1;
                break;
            }
        
        }
        
        for(int i=ridx; i>=0; i--){
            int value = Character.getNumericValue(n.charAt(i))-next;
            next=0;
            if(value >= x) break;
            else if(value >= y) {
                answerList[i] = y;
                break;
            }
            else if(value < y){
                answerList[i] = x;
                next = 1;
            }
        }
        if(next == 1) answerList[0] = 0;
        //앞에서부터 0 지우기
        int zidx = 0;
        for(int i=0;i<answerList.length;i++){
            if(answerList[i] == 0) zidx++;
            else break;
        }
        answerList = Arrays.copyOfRange(answerList, zidx, answerList.length);
        if(answerList.length == 0) return "-1";
        return String.join("",Arrays.stream(answerList).mapToObj(String::valueOf).collect(Collectors.joining("")));
    }

    public static String Solution(String n, int x, int y){
        if(x<y){
            int tmp = y;
            y = x;
            x = tmp;
        }
        StringBuilder answer = new StringBuilder("");

        int idx = -1;
        int cht = 0;
        while(++idx <n.length() && idx >= 0){
            int idxVal = Integer.parseInt(String.valueOf(n.charAt(idx)));
            if(cht<0 && idxVal > y){
                cht=0;
                idxVal-=1;
            }
            if(cht == 1)answer.append(x);
            else if(idxVal > x ){
                answer.append(x);
                cht=1;
            }else if(idxVal == x) answer.append(x);
            else if(idxVal > y) {
                answer.append(y);
                cht=1;
            }
            else if(idxVal == y )answer.append(y);
            else if(idxVal < y && cht == 0){
                answer.replace(idx-1,idx-1,String.valueOf(x));
                cht=-1;
                idx-=2;
            }else if(idxVal < y && cht < 0){
                idx-=2;
            }
            

        };

        if(answer.toString()=="") return "-1";
        return answer.toString();
    }
    
}


/*


4

16 1 3

2 6 9

5 0 8

422223324 2 4

442133 2 4
> 424444

222133 2 4
> 44444
4 0 0
 */