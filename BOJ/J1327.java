package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class J1327 {
    static int n,k;
    static int[] seq;
    static int MAX_CNT;
    static Queue<int[]> que;
    static Set<Integer> cont;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        MAX_CNT = (n-k+1)*(n-k+1)+1;
        seq = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        que = new LinkedList<>();
        cont = new HashSet<>();
        que.add(new int[]{0,serialize(seq)});
        // cont.add(serialize(seq));
        while(que.size() > 0){
            int[] x = que.poll();
            // cont.remove(serialize(x));
            int cnt = x[0];
            int[] s = desereialize(x[1]);
            if(asc(s)){
                System.out.println(cnt);
                return;
            }
            // if(cnt > n*n) break;
            if(cont.contains(x[1])) continue;
            cont.add(x[1]);
            for(int i=0; i<=n-k; i++){
                reverse(s, i);
                int serialS = serialize(s);
                que.add(new int[]{cnt+1,serialS});
                reverse(s,i);
            }
        }
        System.out.println(-1);
    }


    public static boolean asc(int[] s){
        for(int i=1; i<s.length; i++){
            if(s[i-1]> s[i]) return false;
        }
        return true;
    }
    public static void reverse(int[] s, int idx){
        for(int i=0; i< k/2; i++){
            int tmp = s[idx+i];
            s[idx+i] = s[idx+k-1-i];
            s[idx+k-1-i] = tmp;
        }
    }
    public static int serialize(int[] s){
        int x=0;
        for(int i=0;i<s.length;i++){
            x+=Math.pow(10,i) * s[i];
        }
        return x;
    }
    public static int[] desereialize(int x){
        int[] s = new int[n];
        for(int i=0; i<n; i++){
            s[i] = x%10;
            x/=10;
        }
        return s;
    }
    
}
