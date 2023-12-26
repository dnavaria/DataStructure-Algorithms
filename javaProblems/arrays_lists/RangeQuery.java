package arrays_lists;

import java.util.ArrayList;

public class RangeQuery {
    public ArrayList<Long> rangeSum(ArrayList<Integer> A, ArrayList<ArrayList<Integer>> B) {
        int N = A.size();
        ArrayList<Long> prefix = new ArrayList<>();
        prefix.add((long)A.get(0));
        long prefix_value = 0;
        for(int i=1; i< N; i++){
            prefix_value = prefix.get(i-1) + A.get(i);
            prefix.add((long)prefix_value);
        }
        int L = -1, R = -1;
        ArrayList<Long> result = new ArrayList<Long>();
        for (ArrayList<Integer> query : B) {
            L = query.get(0);
            R = query.get(1);
            if (L == 0) result.add(prefix.get(R));
            else result.add((prefix.get(R) - prefix.get(L - 1)));
        }
        return result;
    }
}
