package arrays_lists;

import java.util.ArrayList;

public class SecondLargestElement {
    public int solve(ArrayList<Integer> A){
        int current_largest = -1;
        int prev_largest = -1;
        for (int current_value : A) {
            if(current_value > current_largest){
                prev_largest = current_largest;
                current_largest = current_value;
            }else if (prev_largest < current_value && current_value < current_largest){
                prev_largest = current_value;
            }
        }
        return prev_largest;
    }
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        a.add(2);a.add(1);a.add(2);
        int result = new SecondLargestElement().solve(a);
        System.out.println(result);

    }
}
