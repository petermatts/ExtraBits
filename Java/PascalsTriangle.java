import java.util.ArrayList;

/**
 * PascalTriangle.java
 * 
 * I was working on APCS CH8 PP9 and decided to take it above
 * and beyond the scope of the 1 recursion problem
 * 
 * I have made a fully function class that creates a Pascal's Triangle
 * and has methods to increase the size calculated as well as returning
 * a single line at a specfied index or a toString that will return a
 * formatted String of the entire triangle!
 * 
 * Matthew Peters 5/21/2020
 */

public class PascalsTriangle {
    private final int defaultStartSize = 5;
    private ArrayList<int[]> triangle = new ArrayList<int[]>();
    private int size = defaultStartSize;

    /**
     * Constucts Pascals Triangle to a default size of 5
     */
    public PascalsTriangle() {
        makeTriangle(defaultStartSize);
    }

    /**
     * Constructs Pascals Triangle to initSize
     * @param initSize size to initialize to
     */
    public PascalsTriangle(int initSize) {
        size = initSize;
        makeTriangle(initSize);
    }

    /**
     * makes triangle to specified line number (size)
     * @param size size to make triangle 
     */
    private void makeTriangle(int size) {
        for(int i = 0; i < size; i++) 
            triangle.add(findLine(i+1));
    }

    /**
     * @return ArrayList<int[]> triangle
     */
    public ArrayList<int[]> getTriangle() {
        return triangle;
    }

    /**
     * @param index line number to return must be >=1
     * @return int[] line of specified index
     */
    public int[] getLine(int index) {
        return triangle.get(index-1);
    }

    /**
     * @return size of triangle
     */
    public int size() {
        return size;
    }

    /**
     * Increases size of pascals triangle by adding new lines
     * @param increase amount to increase size by
     */
    public void increaseSize(int increase) {
        for(int i = triangle.size(); i < size+increase; i++)
            triangle.add(findLine(i+1, triangle.get(i-1)));
        size += increase;
    }

    /**
     * @param index index of line to be returned as a string
     * @return string representation of a line in pascals triangle
     */
    public String lineString(int index) {
        int[] array = getLine(index);
        String line = "";

        for(int i = 0; i < array.length; i++) {
            if(i != array.length-1)
                line += array[i] + " ";
            else
                line += array[i];
        }

        return line;
    }

    /**
     * @return a atlest somewhat formated Pascal's Triangle String
     * Formating is neatest on lines 1-5
     */
    public String toString() {
        String pascal = "";
        String bottomLine = lineString(size);
        final int BLMI = bottomLine.length()/2; //Bottom Line Middle Index

        for(int i = 1; i < size; i++) {
            String spacing = "";
            String line = lineString(i);
            int LMI = line.length()/2; //Line Middle Index
            for(int j = 0; j < BLMI-LMI; j++)
                spacing += " ";

            pascal += spacing + line + "\n";
        }
        return pascal + bottomLine;
    }

    /**
     * PRECONDIDTION: n >= 1
     * @param n
     * @return
     */
    private int[] findLine(int n) {
        int[] line = {1};
        if(n==1)
            return line;
        else
            return findLine(n, line);
    }

    /**
     * PRECONDITION n>=1
     * 
     * Indirect recursive method with findLine(int n)
     * @param n
     * @param prevLine
     * @return
     */
    private int[] findLine(int n, int[] prevLine) {
        int[] newLine = new int[prevLine.length+1];

        newLine[0] = 1;
        newLine[newLine.length-1] = 1;

        for(int i = 1; i < prevLine.length; i++)
            newLine[i] = prevLine[i-1] + prevLine[i];

        if(newLine.length == n)
            return newLine;
        else
            return findLine(n, newLine);
    }

    public static void main(String[] args) {
        PascalsTriangle tri = new PascalsTriangle();
        System.out.println();
        System.out.println(tri);
    }
}