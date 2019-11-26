class Solution {
    public int[] solution(int[] prices) {
        int[] ret = new int[prices.length];
		
		for(int i=0;i<prices.length-1;i++) {
			int tmp=0;
			for(int j=i;j<prices.length;j++) {
				if(i==j)continue;
				if(prices[i]<=prices[j]&&j!=prices.length-1) {
					tmp++;
				}else {
					tmp++;
					ret[i]=tmp;
					break;
				}
			}
		}
        return ret;
    }
}