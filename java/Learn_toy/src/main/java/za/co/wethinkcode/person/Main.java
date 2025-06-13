package za.co.wethinkcode.person;

public class Main {
    public static void main(String[] args) {


        World world1 = new World(5, 6);

        Robot robot1 = new Robot(2, 2, world1);

        System.out.println( robot1.getPosition());
        robot1.Move(2, 1);
        System.out.println( robot1.getPosition());
        robot1.Move(10, 10);
        System.out.println( robot1.getPosition());






    }
}