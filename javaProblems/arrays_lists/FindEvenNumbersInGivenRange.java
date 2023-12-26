package arrays_lists;
import java.util.ArrayList;
public class FindEvenNumbersInGivenRange {
    public ArrayList<Integer> solve(ArrayList<Integer> A, ArrayList<ArrayList<Integer>> B) {
        //  A.replaceAll(integer -> integer % 2 == 0 ? 1 : 0);
        // or
        for(int i=0; i<A.size();i++){
            A.set(i, A.get(i) % 2 == 0 ? 1 : 0);
        }
        for(int i=1; i<A.size();i++){
            A.set(i, A.get(i) + A.get(i-1));
        }
        ArrayList<Integer> result = new ArrayList<Integer>();
        int L = -1, R = -1;
        for(ArrayList<Integer> query: B){
            L = query.get(0);
            R = query.get(1);
            if(L==0) result.add(A.get(R));
            else result.add(A.get(R) - A.get(L-1));
        }
        return result;
    }
}
