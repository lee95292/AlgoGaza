package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class S12837 {
    public static class SegTree{
        long[] tree;
        int treeSize;
        SegTree(long initSize){
            int h = (int)Math.ceil(Math.log(initSize) / Math.log(2))+1;
            this.treeSize= (int)Math.pow(2,h);
            this.tree = new long[treeSize];
        }

        public long init(int[] arr, int node, int start, int end){
            if(start == end){
                return tree[node] = arr[start];
            }
            return tree[node] = init(arr, node*2, start, (start+end)/2) + init(arr, node*2+1, (start+end)/2+1, end);
        }

        public void update(int[] arr, int node,int idx, int diff, int start, int end){
            if( idx < start || idx > end){
                return;
            }

            tree[node] += diff;
            if(start == end) return;

            update(arr, 2*node, idx, diff, start, (start+end)/2);
            update(arr, 2*node+1, idx, diff, (start+end)/2+1, end);
        }
        public long sum(int[] arr, int node, int start, int end, int left, int right){
            if(start > right || end < left) return 0;

            if(left <= start && end <= right) return tree[node];
            return sum(arr, 2*node, start, (start+end)/2, left, right) + sum(arr, 2*node+1, (start+end)/2+1, end, left, right);

        }
        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            for(int i=1; i<=Math.log(treeSize)/Math.log(2);i++){
                sb.append(" ".repeat((int)Math.pow(2,5-i)));
                for(int j=(int)Math.pow(2,i-1); j<Math.pow(2,i);j++){
                    sb.append(" "+tree[j]);
                }
                sb.append("\n");
            }
            return sb.toString();
        }
    }
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int[] arr = new int[n+1];
        StringBuilder sb = new StringBuilder();
        SegTree segTree = new SegTree(n);
        for(int i=0; i<q; i++){
            int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
            if(input[0] == 1){
                segTree.update(arr, 1, input[1], input[2], 1,n);
                arr[input[1]] += input[2];
            }
            if(input[0]==2){
                sb.append(segTree.sum(arr, 1, 1,n, input[1], input[2])).append('\n');
                // System.out.println();
            }
        }
        System.out.println(sb.toString());
        
    }
}


/*
99 3
1 1 1
1 1 1
2 1 1

10 7
1 3 10000
1 4 -5000
1 7 -3000
1 10 4000
2 1 10
1 6 35000
2 4 10
 */