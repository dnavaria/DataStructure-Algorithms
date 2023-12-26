package arrays_lists;

public class ClosestMinMax {
    public int solve(int[] A) {
        int N = A.length;
        int min = A[0], max = A[0];
        for (int j : A) {
            if (j > max) max = j;
            if (j < min) min = j;
        }
        if (max == min){
            return 1;
        }
        int last_min_index = -1;
        int last_max_index = -1;
        int ans = N;
        for(int i=0;i<N;i++){
            if (A[i] == min) last_min_index = Math.max(i, last_min_index);
            if (A[i] == max) last_max_index = Math.max(i, last_max_index);
            if (last_min_index != -1 && last_max_index != -1){
                ans = Math.min(ans, Math.abs(last_max_index-last_min_index)+1);
            }
        }
        return ans;
    }
}
