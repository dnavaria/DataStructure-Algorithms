package subarrays;

public class MaxSubArray {
    public int maxSubarray(int A, int B, int[] C) {
        int result = 0;
        int max_value = Integer.MIN_VALUE;
        int N = C.length;
        for(int i=0;i<N;i++){
            int sum = 0;
            for(int j=i;j<N;j++){
                sum+=C[j];
                if (sum <= B){
                    max_value = Math.max(sum, max_value);
                }
            }
        }
        return max_value == Integer.MIN_VALUE ? 0 : max_value;
    }
}
