public class RemoveDupFromArr2 {
    public static void main(String[] args){
        int[] arr = {0,0,1,1,1,1,2,3,3};
        System.out.println(removeDuplicates(arr));
    }
    public static int removeDuplicates(int[] nums) {
        if(nums.length <3) return nums.length;
    
        int count = 1;
        // Count duplicate elements
        int dup = 0;
        for(int i=1; i<nums.length; i++) {
            if(nums[i] != nums[i-1]) {
                nums[count] = nums[i];
                count++;
                dup = 0;
            } else if (dup == 0) {
                nums[count] = nums[i];
                count++;
                dup++;
            }
        }
        return count;
    }
}

