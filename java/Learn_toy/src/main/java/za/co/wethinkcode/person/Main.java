package za.co.wethinkcode.person;

public class Main {
    public static void main(String[] args) {

//        first lets create a world

        World robotWold=new World(5,5);

        Robot myRobot=new Robot(2,2,robotWold);

        System.out.println(myRobot.getPosition());

        myRobot.move(1,0);
        System.out.println(myRobot.getPosition());
        myRobot.move(1,1);
        System.out.println(myRobot.getPosition());
        myRobot.move(1,20);
        System.out.println(myRobot.getPosition());
    }




}