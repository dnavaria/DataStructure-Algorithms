package basics;

public class MakeMangoJuice {
    public int solve(int A, int B){
        return (((A*3)+B)/2);
    }
    public static void main(String[] args) {
        int result = new MakeMangoJuice().solve(7, 1);
        System.out.println(result);
    }
}
