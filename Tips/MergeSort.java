package Tips;

import java.util.Arrays;

import javax.swing.text.AbstractDocument.LeafElement;

public class MergeSort {
    public static int[] array,sorted;
    public static int n;
    public static void main(String[] args) {
        array = new int[]{5,4,2,1,7,3,6};
        n = 7;
        sorted = new int[n];
        mergeSort(0,n-1);
        System.out.println(Arrays.toString(array));

    }
    public static void mergeSort(int start, int end){
        int mid = (start+end)/2;
        if(start<end){
            mergeSort(start, mid);
            mergeSort(mid+1, end);
            merge(start, mid, end);
        }
    }

    public static void merge(int start,int mid, int end){
        int lidx = start, ridx = mid+1, sidx = start;
        while(lidx <= mid && ridx <= end){
            if(array[lidx]<array[ridx])
                sorted[sidx++] = array[lidx++];
            else
                sorted[sidx++] = array[ridx++];
        }
        for(int i=lidx; i<=mid;i++){
            sorted[sidx++] = array[i];
        }
        for(int i=ridx; i<=end; i++){
            sorted[sidx++] = array[i];
        }
        for(int i=start; i<=end; i++){
            array[i] = sorted[i];
        }
    }
}
