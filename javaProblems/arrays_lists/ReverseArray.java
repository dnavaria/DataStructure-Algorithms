package arrays_lists;

import java.util.ArrayList;
import java.util.List;

public class ReverseArray {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public ArrayList<Integer> solve(final List<Integer> A) {
        ArrayList<Integer> a = new ArrayList<>();
        int i = A.size() - 1;
        while (i > -1){
            a.add(A.get(i));
            i--;
        }
        return a;
    }
}
