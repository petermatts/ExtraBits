//Sample code given using the <random> library

#include <iostream>
#include <random>
#include <ctime>
using namespace std;
const int sides = 6;
int main(void) {
    const int n_dice = 2;
    uniform_int_distribution<unsigned> u(1,6);
    default_random_engine e(time(0));
    cout << "\nEnter number of trials: ";
    int trials;
    cin >> trials; //compare to scanf
    int* outcomes = new int[n_dice * sides +1];
    for (int j = 0; j < trials; ++j) {
        int roll = 0;
        for (int k = 1; k <= n_dice; ++k) {
            roll += u(e);
        }
        outcomes[roll]++;
    }
    cout << "probability\n";
    for (int j = 2; j < n_dice * sides + 1; ++j)
        cout << "j = " << j << " p = " << static_cast<double>(outcomes[j])/trials << endl;
}