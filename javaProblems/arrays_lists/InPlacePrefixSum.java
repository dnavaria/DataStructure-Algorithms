package arrays_lists;
import java.util.ArrayList;

public class InPlacePrefixSum {
    public ArrayList<Integer> solve(ArrayList<Integer> A) {
        for(int i=1;i<A.size();i++){
            A.set(i, A.get(i) + A.get(i-1));
        }
        return A;
    }
}
