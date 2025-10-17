package Coordinate;

public class Point {
    /**
     * x: The x coordinate y: The y coordinate z: The z coordinate
     */
    protected double x, y, z;
    private double theta;
    private double r;
    private double phi;
    private double rho;

    public double x() {
        return x;
    }

    public double y() {
        return y;
    }

    public double z() {
        return z;
    }

    public double theta() {
        return theta;
    }

    public double r() {
        return r;
    }

    public double phi() {
        return phi;
    }

    public double rho() {
        return rho;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void setZ(double z) {
        this.z = z;
    }

    public void setTheta(double theta) {
        this.theta = theta;
    }

    public void setR(double r) {
        this.r = r;
    }

    public void setPhi(double phi) {
        this.phi = phi;
    }

    public void setRho(double rho) {
        this.rho = rho;
    }
}
