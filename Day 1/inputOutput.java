import java.util.Scanner;

public class inputOutput {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter anything: ");
        
        String inputString = scanner.nextLine();
        Integer input = Integer.parseInt(inputString);
        System.out.println("You entered: " + input);
        scanner.close();
    }
}