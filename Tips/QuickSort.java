package Tips;

public class QuickSort {
    static int[] array;
    static int n;

    public static void main(String[] args) {
        array = new int[] { 5, 3, 2, 7, 1, 4, 6 };
        n = 7;
        QuickSort(0, n - 1);
    }

    public static void QuickSort(int start, int end) {
        System.out.println(start+" "+end);
        int pivot = array[start];
        int left = start + 1;
        int right = end;
        while (left < right) {
            while (left < right && array[left] < pivot)
                left++;
            while (left < right && array[right] > pivot)
                right--;
            if(array[left] > array[right]){
                int tmp = array[left];
                array[left] = array[right];
                array[right] = tmp;
            }
        }
        array[left] = array[start];
        array[start] = pivot;
        if(left<right){
            QuickSort(start+1, left-1);
            QuickSort(left+1, end);
        }

    }
}
