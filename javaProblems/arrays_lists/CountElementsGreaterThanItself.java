package arrays_lists;
import java.util.ArrayList;

public class CountElementsGreaterThanItself {
    public int solve1(ArrayList<Integer> A) {
        int count = 0;
        for(int i=0; i<A.size(); i++){
            int current_val = A.get(i);
            for (int val : A) {
                if (val > current_val) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }

    public int solve(ArrayList<Integer> A){
        int count = 0;
        int max_so_far = A.get(0);
        int max_value_count = 1;
        for(int i = 1; i < A.size(); i++){
            int current_value = A.get(i);
            if(current_value > max_so_far){
                max_so_far = current_value;
                max_value_count = 1;
            }
            else if(current_value == max_so_far){
                max_value_count++;
            }
        }
        return (A.size()) - max_value_count;
    }

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        a.add(7);a.add(4);a.add(2);a.add(10);a.add(10);
        int result = new CountElementsGreaterThanItself().solve(a);
        System.out.println(result);
    }
}
