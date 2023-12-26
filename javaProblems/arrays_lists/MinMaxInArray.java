package arrays_lists;

import java.util.ArrayList;

public class MinMaxInArray {
    public int solve(ArrayList<Integer> A) {
        int max_so_far = -1000000000;
        int min_so_far = 1000000000;
        for (Integer integer : A) {
            if (integer > max_so_far) max_so_far = integer;
            if (integer < min_so_far) min_so_far = integer;
        }
        return max_so_far + min_so_far;
    }
    public static void main(String[] args) {
         ArrayList<Integer> a = new ArrayList<>();
         a.add(1);
         a.add(5);
         a.add(9);
//         a.add(1);
//         a.add(3);
         int result = new MinMaxInArray().solve(a);
         System.out.println(result);
    }
}
