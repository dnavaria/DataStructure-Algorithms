package basics;

public class SqrtOfANumber {
    public int solve(int A){
        for (int i = 1; i*i <= A; i++) {
            if (i*i == A) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int result = new  SqrtOfANumber().solve(25);
        System.out.println(result);
    }
}
