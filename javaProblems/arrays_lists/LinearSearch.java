package arrays_lists;

import java.util.ArrayList;

public class LinearSearch {
    public int solve(ArrayList<Integer> A, int B) {
        int count = 0;
        for(Integer current_value: A){
            if(current_value == B) count++;
        }
        return count;
    }
}
