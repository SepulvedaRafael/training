import java.io.IOException;
import java.util.Scanner;

public class URI1002 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        double n = 3.14159;
        double raio = sc.nextDouble();

        double area = n * (raio * raio);
        System.out.println(String.format("A=%.4f", area));
        sc.close();
    }
}
