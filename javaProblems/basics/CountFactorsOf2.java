package basics;

public class CountFactorsOf2 {
    public int solve(int A){
        int count = 0;
        for (int i = 1 ; i*i<=A ; i++){
            if (A % i == 0) {
                if (i==A/i) count+=1;
                else count+=2;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        int result = new CountFactorsOf2().solve(10);
        System.out.println(result);
    }
}
