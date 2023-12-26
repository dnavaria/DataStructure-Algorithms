package subarrays;

public class SubArrayInAGivenRange {
    public int[] solve(int[] A, int B, int C) {
        int N = C - B + 1;
        int[] result = new int[N];
        int i = 0;
        while(i<N){
            result[i] = A[B];
            i++;
            B++;
        }
        return result;
    }
}
