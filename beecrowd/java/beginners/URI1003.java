import java.io.IOException;
import java.util.Scanner;

public class URI1003 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        System.out.println(String.format("SOMA = %d", A + B));
        sc.close();
    }
}
