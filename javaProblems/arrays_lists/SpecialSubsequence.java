package arrays_lists;

public class SpecialSubsequence {
    public int solve(String A) {
        int count_a = 0;
        int MOD = 1000*1000*1000 + 7;
        int sum = 0;
        for(int i=0;i<A.length();i++){
            if (A.charAt(i) == 'A') count_a++;
            else if (A.charAt(i) == 'G'){
                sum += count_a;
                sum = sum % MOD;
            }
        }
        return sum % MOD;
    }
}
