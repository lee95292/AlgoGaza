package Greedy;

class ChooseBowlingBall {
    public static void main(String[] args){
        // int n = 8;
        // int m = 5;
        // int[] weights = {1,5,4,3,2,4,5,2};

        int n = 5;
        int m = 3;
        int[] weights = {1,3,2,3,2};

        System.out.println(Solution(n, m, weights));
    }   
    
    public static int Solution(int n, int m, int[] weights){
        int answer = 0;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if(i==j || weights[i] == weights[j]){
                    continue;
                }
                answer+=1;
            }
        }
        return answer;
    }
    
}
