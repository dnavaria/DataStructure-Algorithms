package arrays_lists;

public class BulbsProblem {
    public int bulbs(int[] A) {
        int count = 0;
        int N = A.length;
        boolean isFlipped = false;
        for (int j : A) {
            if (isFlipped) {
                if (j == 1) {
                    count++;
                    isFlipped = false;
                }
            } else {
                if (j == 1) continue;
                else if (j == 0) {
                    isFlipped = true;
                    count++;
                }
            }

        }
        return count;
    }
}
