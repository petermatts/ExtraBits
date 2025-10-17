package Coordinate;

public class CartesianPoint extends Point {
    public CartesianPoint(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public CylindricalPoint Cylindrical() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.atan(y / x);
        return new CylindricalPoint(r, theta, z);
    }

    @Override
    public String toString() {
        return "Rectangular: (x: " + x + " , y: " + y + " , z: " + z + ")\n";
    }
}
