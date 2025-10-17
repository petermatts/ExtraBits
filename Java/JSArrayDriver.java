public class JSArrayDriver {
    public static void main(String[] args) {
        Object a = new Object();
        int intA = 5;
        char charA = 'a';
        String strA = "Hello World";
        double doubA = 5.0;
        boolean booA = true;

        // a = intA;
        // System.out.println(a + "\t" + a.getClass());
        // a = charA;
        // System.out.println(a + "\t" + a.getClass());
        // a = strA;
        // System.out.println(a + "\t" + a.getClass());
        // a = doubA;
        // System.out.println(a + "\t" + a.getClass());
        // a = booA;
        // System.out.println(a + "\t" + a.getClass());
        // a = new PascalsTriangle();
        // System.out.println(a + "\t" + a.getClass());

        JSArray array = new JSArray();
        array.push(a);
        array.push(intA);
        array.push(charA);
        array.push(booA);
        array.push(strA);
        array.push(doubA);

        System.out.println(array);
        System.out.println(array.length);
    }
}
