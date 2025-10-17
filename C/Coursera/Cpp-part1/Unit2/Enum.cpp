//Ira Pohl
//Copyright 2016
//Supplementary example on overloading operator

#include<iostream>
#include<cstdint>
using namespace std;

enum class days:int8_t { SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY };

//unlike plain enums C++11 enum class is typesafe and does not silently
//convert to int

ostream &operator<<(ostream &out, const days &d) {
    out << static_cast<int>(d);
    return out;
}

days operator++(days &d) { //PREFIX OPERATOR
    d = static_cast<days>((static_cast<int>(d) + 1) % 7);
    return d;
}

days operator++(days &d, int) { //POSTFIX OPERATOR
    days temp = d;
    d = static_cast<days>((static_cast<int>(d) + 1) % 7);
    return temp;
}

int main()
{
    days today{days::MONDAY};
    cout << "Demonstrate class enum" << endl;
    cout << "MONDAY VALUE IS " << today << endl;
    cout << "INCREMENT VALUE IS " << ++today << endl;
    cout << "INCREMENT VALUE IS " << today++ << endl;
    cout << "INCREMENT VALUE IS " << today << endl;
    return 0;
}