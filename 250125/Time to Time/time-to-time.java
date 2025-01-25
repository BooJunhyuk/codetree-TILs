import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언 및 입력:
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt(); 
        int d = sc.nextInt();
        
        // 출력
        System.out.println((c * 60 + d) - (a * 60 + b));
    }
}
