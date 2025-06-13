package za.co.wethinkcode.person;

public class World {
    private int width;
    private int height;

    public World(int width, int height){
        this.width=width;
        this.height=height;ffvfv
    }

    public boolean isValidPosition(int x, int y){
        return x>=0 && x<width && y>=0 && y<height;
    }



}
