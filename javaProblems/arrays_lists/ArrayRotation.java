package arrays_lists;

import java.util.ArrayList;

public class ArrayRotation {
    public ArrayList<Integer> ReverseArray(ArrayList<Integer> A, int B, int C) {
        while (B < C){
            int temp = A.get(B);
            A.set(B, A.get(C));
            A.set(C, temp);
            B++;
            C--;
        }
        return A;
    }
    public ArrayList<Integer> solve(ArrayList<Integer> A, int B) {
        B = B % A.size();
        ReverseArray(A, 0, A.size()-B-1);
        ReverseArray(A, A.size()-B, A.size()-1);
        ReverseArray(A, 0, A.size()-1);
        return A;
    }
}
