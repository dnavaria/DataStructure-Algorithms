package arrays_lists;
import java.util.ArrayList;

public class EquilibriumIndex {
    public int solve1(ArrayList<Integer> A) {
        int N = A.size();
        for(int i = 1; i < N; i++){
            int pf_value = A.get(i-1) + A.get(i);
            A.set(i, pf_value);
        }
        int lsum = 0, rsum = 0;
        for(int i=0; i < N; i++){
            if (i>0) lsum = A.get(i-1);
            rsum = A.get(N-1) - A.get(i);
            if (lsum == rsum) return i;
        }
        return -1;
    }

    public int solve(ArrayList<Integer> A){
        int N = A.size();
        int sum = 0;
        int leftSum = 0;
        for(Integer val: A){
            sum+=val;
        }
        for(int i=0;i<N;i++){
            sum-=A.get(i);
            if (leftSum == sum) return i;
            leftSum+=A.get(i);
        }
        return -1;
    }


    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        a.add(-7);a.add(1);a.add(5);a.add(2);a.add(-4);a.add(3);a.add(0);
        System.out.println(new EquilibriumIndex().solve(a));
    }
}
