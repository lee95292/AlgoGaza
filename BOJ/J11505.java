package BOJ;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J11505 {
    static class SegTree {
        long[] tree;
        int treeSize;
        static int MOD = 1000000007;

        SegTree(int initSize) {
            int h = (int) Math.ceil(Math.log(initSize) / Math.log(2)) + 1;
            treeSize = (int) Math.pow(2, h);
            tree = new long[treeSize];
            Arrays.fill(tree, 1);
        }

        public long init(long[] arr, int node, int start, int end) {
            // System.out.println(String.format(" node %d | start %d | end %d" , node,
            // start, end ));
            if (end == start) {
                if (start >= arr.length)
                    return 1;
                return tree[node] = arr[start];
            }
            return tree[node] = (init(arr, 2 * node, start, (start + end) / 2)
                    * init(arr, 2 * node + 1, (start + end) / 2 + 1, end)) % MOD;
        }

        public long update(int node, int idx, long diff, int start, int end) {
            if (idx < start || idx > end)
                return tree[node];
            if (start == end)
                return tree[node] = diff;
            return tree[node] = (update(2 * node, idx, diff, start, (start + end) / 2) * update( 2 * node + 1, idx, diff, (start + end) / 2 + 1, end))%MOD;
        }

        public long query(int node, int start, int end, int left, int right) {
            if (start > right || end < left)
                return 1L;

            if (left <= start && end <= right) {
                return tree[node];
            }
            return (query(2 * node, start, (start + end) / 2, left, right)
                    * query( 2 * node + 1, (start + end) / 2 + 1, end, left, right)) % MOD;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            // sb.append("\n");
            for (int i = 1; i <= (Math.log(treeSize) / Math.log(2)); i++) {
                sb.append("  ".repeat((int) (Math.log(treeSize) / Math.log(2)) - i));
                for (int j = (int) Math.pow(2, i - 1); j < Math.pow(2, i); j++) {
                    sb.append(tree[j] + "  ");
                }
                sb.append("\n");
            }
            return sb.toString();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(v -> Integer.parseInt(v)).toArray();
        int n = input[0], m = input[1], k = input[2];
        long[] arr = new long[n + 1];
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        SegTree segTree = new SegTree(n);
        segTree.init(arr, 1, 1, segTree.treeSize / 2);
        // System.out.println(segTree);
        for (int i = 0; i < m + k; i++) {
            long[] in = Arrays.stream(br.readLine().split(" ")).mapToLong(v -> Long.parseLong(v)).toArray();
            if (in[0] == 1) {
                //(int node, int idx, long diff, int start, int end)
                segTree.update(1, (int)in[1], in[2], 1, segTree.treeSize / 2);
            } else if (in[0] == 2) {
                arr[(int)in[1]] = in[2];
                sb.append(segTree.query(1, 1, segTree.treeSize / 2, (int)in[1], (int)in[2])).append("\n");
            }
            // System.out.println(Arrays.toString(in));
            // System.out.println(segTree);
        }
        System.out.println(sb.toString());
    }
}
