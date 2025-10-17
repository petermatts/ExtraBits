import java.util.List;
import java.util.ArrayList;

/**
 * This class was created because I was very bored and thought to myself Java
 * and JavaScript are very similar but also very different especially when it
 * comes to arrays.
 * 
 * So behold, this class is a Java implementation of a js array
 */
public class JSArray {
    /* Properties */

    protected int length = 0;
    private ArrayList<Object> array;

    /* Support for java integration */

    //public String getElementType() {
        //
    //}

    /**
     * @return a formated printable String representation of the JSArray Object
     * Each element is printed as its own String representation if it is a Java
     * primitive type or a String (Strings will be surrounded by double quotes
     * Characters will be surrounded by single quotes)
     * 
     * Otherwise result of the elements Object.getClass() is printed
     */
    @Override
    public String toString() {
        String str = "[";
        final String seperator = ", ";

        for(int i = 0; i < array.size(); i++) {
            Object e = array.get(i);
            if((e instanceof Boolean) || (e instanceof Byte) || (e instanceof Short) || (e instanceof Integer) || (e instanceof Long) || (e instanceof Float) || (e instanceof Double))
                str += (e.toString() + ((i==array.size()-1) ? "" : seperator));
            else if(e instanceof String)
                str += ("\"" + e + "\"" + ((i==array.size()-1) ? "" : seperator));
            else if(e instanceof Character)
                str += ("\'" + e + "\'" + ((i==array.size()-1) ? "" : seperator));
            else
                str += (e.getClass().getSimpleName() + ((i==array.size()-1) ? "" : seperator));
        }

        return str += "]";
    }

    /* Constructors */

    public JSArray() {
        this.array = new ArrayList<>();
        this.length = array.size();
    }

    public JSArray(List<Object> list) { //?Object ... elem
        this.array = new ArrayList<>(list);
        this.length = array.size();
    }

    public JSArray(int size) {
        this.array = new ArrayList<>(size);
        this.length = size;
    }

    /* Static Methods */

    public static JSArray from() {return null;}
    public static boolean isArray() {return false;}
    public static JSArray of() {return null;}
    
    
    /* non Static Methods */

    /**
     * Merges this JSArray with another JSArray
     * @param o
     * @return a NEW JSArray
     */
    public JSArray concat(JSArray o) {return null;}
    public JSArray copyWithin(int start, int end, int place) {return null;}
    // public ___? entries() {}
    //public boolean every(boolean condition???) {return false;}
    public JSArray fill(int fillWith, int start, int end) {return null;}


    /**
     * @param o
     * @return the new length of the array
     */
    public int push(Object o) {
        array.add(o);
        length = array.size();
        return length;
    }
}