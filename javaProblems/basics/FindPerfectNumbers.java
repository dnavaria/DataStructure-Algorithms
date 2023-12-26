package basics;

public class FindPerfectNumbers {

    public int solve(int A){
        int result = 0;
        for (int i = 1; i<A; i++){
            if (A % i == 0){
                result+=i;
            }
        }
        return result == A ? 1 : 0;
    }
    public static void main(String[] args) {
        int result = new FindPerfectNumbers().solve(49);
        System.out.println(result);
    }
}
