package subarrays;

import java.util.ArrayList;

public class GenerateAllSubArrays {
    public ArrayList<ArrayList<Integer>> solve(ArrayList<Integer> A) {
        int N = A.size();
        ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();
        for(int i=0;i<N;i++){
            for(int j=i;j<N;j++){
                ArrayList<Integer> arr = new ArrayList<>();
                for(int k=i;k<=j;k++){
                    arr.add(A.get(k));
                }
                matrix.add(arr);
            }
        }
        return matrix;
    }
}
