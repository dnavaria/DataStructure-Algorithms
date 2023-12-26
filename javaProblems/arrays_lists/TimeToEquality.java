package arrays_lists;

import java.util.ArrayList;

public class TimeToEquality {
    public int solve(ArrayList<Integer> A){
        int count = 0;
        // find max element in array;
        int max_value = -1;
        for(Integer current_value: A){
            if (current_value > max_value) max_value = current_value;
        }
        for(Integer current_value: A){
            if (current_value == max_value) continue;
            count += max_value - current_value;
        }
        return count;
    }
}

