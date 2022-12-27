/**
 * https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
 * 내부적으로 객체를 생성하는 문제이므로, 해당 코드는 실행이 안됩니다.
 * 
 * Accumulate sum, DFS
 */

// public class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;

//     TreeNode() {
//     }

//     TreeNode(int val) {
//         this.val = val;
//     }

//     TreeNode(int val, TreeNode left, TreeNode right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }

public class MaxWay2Split {
    public static void main(String[] args) {

    }

    static long maxvalue;
    public static int maxProduct(TreeNode root) {
        sumDfs(root);
        
        return findDfs(root, 0, root.val)% (int)(Math.pow(10,9) + 7);
    }  

    public static int sumDfs(TreeNode node){
        if(node == null) return 0;

        int sumValue = sumDfs(node.left) + sumDfs(node.right) + node.val;
        node.val = sumValue;
        return sumValue;
    }

    public static void findDfs(TreeNode node,int maxv, int sum){
        if(node == null) return;

        maxvalue = Math.max(maxvalue, node.val*(sum-node.val));
        findDfs(node.left, maxvalue, sum);
        findDfs(node.right, maxvalue, sum);
    }

}
