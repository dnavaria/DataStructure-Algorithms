package arrays_lists;

public class BestTimeToBuyStocks1 {
    public int maxProfit(final int[] A) {
        int N = A.length;
        if (N == 0) return 0;
        int max_profit = 0;
        int min_val = A[0];
        for(int i=1;i<N;i++){
            if (A[i] < min_val) min_val = A[i];
            int current_profit = A[i] - min_val;
            if(current_profit > max_profit) max_profit = current_profit;
        }
        return max_profit;
    }
}
