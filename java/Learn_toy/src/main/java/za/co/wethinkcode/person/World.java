package za.co.wethinkcode.person;

public class World {
    private final int width;
    private final int height;

    //constructor
    public World(int width, int height){
        this.width=width;
        this.height=height;
    }

    //Method to check if a position is within the world

    public boolean isValidPosition(int x, int y){
        return x >=0 && x< width && y >=0&& y<height;
    }


}
