package arrays_lists;

import java.util.Arrays;

public class ProductExceptSelf {
    public int[] solve(int[] A) {
        int N = A.length;

        int[] prefix = new int[N];
        prefix[0] = A[0];
        for(int i=1;i<N;i++){
            prefix[i] = prefix[i-1] * A[i];
        }

        int[] suffix = new int[N];
        suffix[N-1] = A[N-1];
        for(int i = N - 2; i > -1; i--){
            suffix[i] = suffix[i+1] * A[i];
        }

        int[] result = new int[N];
        for(int i=0;i<N;i++){
            if(i==0){
                result[i] = suffix[i+1];
            }else if(i == N-1){
                result[i] = prefix[i-1];
            }else{
                result[i] = prefix[i-1] * suffix[i+1];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = new ProductExceptSelf().solve(arr);
        System.out.println(Arrays.toString(result));
    }
}
