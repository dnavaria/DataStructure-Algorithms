package basics;

public class ReturnPrime {
    public int GetFactors(int A){
        int count = 0;
        for (int i=1;i*i<=A;i++){
            if (A%i==0){
                if (i == A / i) count+=1;
                else count+=2;
            }
        }
        return count;
    }
    public int solve(int A){
        int count = 0;
        for (int i=2;i<=A;i++){
            if (GetFactors(i) == 2) count+=1;
        }
        return count;
    }
    public static void main(String[] args) {
        int result = new ReturnPrime().solve(19);
        System.out.println(result);
    }
}

