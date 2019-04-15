import java.util.Scanner;

public class Number {
    static Scanner stdin = new Scanner(System.in);
    Integer num;

    public static void main(String[] args) {
        Number num = new Number();
        num.run();
    }

    public void run() {
        num = userInput();
        printNums(num);
    }

    public Integer userInput() {
        while(true) {
            System.out.print("Number:\n");
            num = stdin.nextInt();
            if (num > 0) {
                return num;
            } else {
                continue;
            }
        }
    }

    public void printNums(Integer num) {
        for(int i = 1; i < num; i++) {
            System.out.print(i + ": " + evenOrOdd(i) + "\n");
        }
    }

    public String evenOrOdd(Integer num) {
        if (num %  2 == 0) {
            return "even";
        } else {
            return "odd";
        }
    }
}
