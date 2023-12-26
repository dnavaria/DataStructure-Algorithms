package arrays_lists;

import java.util.ArrayList;

public class ReverseInRange {
    public ArrayList<Integer> solve(ArrayList<Integer> A, int B, int C) {
        while (B < C){
            int temp = A.get(B);
            A.set(B, A.get(C));
            A.set(C, temp);
            B++;
            C--;
        }
        return A;
    }
}
