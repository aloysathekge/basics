package za.co.wethinkcode.person;

public class Robot {

    private int x;
    private int y;
    World world;

    public Robot(int startX, int startY, World world){

        if (world.isValidPosition(startX, startY)) {
            this.x=startX;
            this.y=startY;

        }else{
            this.x=0;
            this.y=0;
        }
        this.world=world;

    }

    public void Move(int deltaX, int deltaY){
        int newX=x+deltaX;
        int newY=x+deltaY;

        if (world.isValidPosition(newX, newY)) {
            x=newX;
            y=newY;

        }



    }

    public String getPosition(){
        return "Robot is at position" + "(" + x + ","+ y +")";    }

















//    private int x ;
//    private int y;
//    private World world;
//
//
//    public Robot(int startX, int startY, World world){
//        if (world.isValidPosition(startX,startY)){
//            this.x=startX;
//            this.y=startY;
//        }else{
//            this.x=0;
//            this.y=0;
//        }
//        this.world=world;
//    }
////    Methods to move the robot
//    public void move (int deltaX, int deltaY){
//        int newX=x+deltaX;
//        int newY=y+deltaY;
//        if (world.isValidPosition(newX,newY)){
//            x=newX;
//            y=newY;
//        }
//    }
//
//    public String getPosition(){
//        return "Robot is at (" +x + ", " +y +")";
//    }

}
