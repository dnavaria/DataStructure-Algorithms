package basics;

public class IsPrime{
    public int solve(int A) {
        int count = 0;
        for (int i = 1; i*i <=A ; i++) {
            if (A % i == 0){
                if ( i ==  A / i) count+=1;
                 else count+=2;
            }
        }
        return count == 2 ? 1 : 0;
    }
    public static void main(String[] args) {
        int result = new IsPrime().solve(11);
        System.out.println(result);
    }
}