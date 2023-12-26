package subarrays;

public class SumOfAllSubArrays {
    public long subarraySum(int[] A) {
        int N = A.length;
        long sum = 0;
        for(int i=0;i<N;i++){
            int s = i + 1;
            int e = N - i;
            long value = (long)s * e * A[i];
            sum=sum + value;
        }
        return sum;
    }
}
