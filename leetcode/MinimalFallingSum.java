/*
 * https://leetcode.com/problems/minimum-falling-path-sum/
 * Simple DP
 */
public class MinimalFallingSum{
    public static void main(String[] args){
        int[][] arr1 = {{-19,57},{-40,-5}};
        int[][] arr2 =  {{2,1,3},{6,5,4},{7,8,9}};
        System.out.println(minFallingPathSum(arr2));

    }

    public static int minFallingPathSum(int[][] matrix) {
        if(matrix.length == 1) return matrix[0][0];

        for(int i=1; i< matrix.length; i++){
            for(int j=0; j<matrix[0].length; j++){
                if(j == 0) 
                    matrix[i][j] += Math.min(matrix[i-1][0], matrix[i-1][1]);
                else if (j == matrix[0].length-1) 
                    matrix[i][j] += Math.min(matrix[i-1][matrix[0].length-1], matrix[i-1][matrix[0].length-2]);
                else 
                    matrix[i][j] += Math.min(Math.min(matrix[i-1][j],matrix[i-1][j+1]),matrix[i-1][j-1]);
            }
        }

        int min = Integer.MAX_VALUE;
        for(int i=0; i< matrix[0].length;i++){
            min = Math.min(min, matrix[matrix.length-1][i]);
        }
        return min;
    }
    
}
