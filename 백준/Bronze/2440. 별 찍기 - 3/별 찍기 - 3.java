import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        for (int i = n; i > 0; i--) {
            String a = "";
            for (int j = 0; j < i; j++) {
                a += "*";
            }
            System.out.println(a);
        }
    }
}