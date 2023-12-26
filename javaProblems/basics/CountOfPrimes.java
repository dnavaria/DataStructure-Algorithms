package basics;

public class CountOfPrimes {
    public int isPrime(int A){
        int count = 0;
        for (int i = 1; i*i <=A ; i++) {
            if (A % i == 0){
                count+=1;
            }
        }
        return count == 2 ? 1 : 0;
    }
    public int solve(int A) {
        int count = 0;
        for (int i = 2; i <= A ; i++) {
            if(isPrime(i) == 1){
                count+=1;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        int result = new CountOfPrimes().solve(50);
        System.out.println(result);
    }
}
