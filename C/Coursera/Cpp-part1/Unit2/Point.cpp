#include <iostream>

using namespace std;

class Point {
    public:
        Point(double x = 0.0, double y = 0.0) { this->x = x; this -> y = y; }
        double getX() { return x; }
        void setX(double v) { x = v; }
        double getY() { return y; }
        void setY(double v) { y = v; }
    private:
        double x, y;
};

Point operator + (Point &p1, Point &p2) {
    Point sum(p1.getX() + p2.getX(), p1.getY() + p2.getY());
    return sum;
}

ostream &operator << (ostream &out, Point &p) {
    out << "(" << p.getX() << "," << p.getY() << ")";
    return out;
}


int main() {
    Point a = { 3.5, 2.5 };
    Point b = { 2.5, 4.5 };
    Point sum = a + b;
    //! cannot use expression a + b with << for some reason
    //! even though that is what is given in lecture video
    cout << "a = " << a << endl << "b = " << b << endl << endl;
    cout << "sum = " << sum << endl;
}
