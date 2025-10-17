#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v(5);

    cout << v.size() << endl;
    for(int i = 0; i < v.size(); i++)
        cout << v[i] << " ";

    cout << endl << endl;

    int size = 4;
    vector<vector<int>> vv(size);

    for(int i = 0; i < vv.size(); i++)
        vv[i] = vector<int>(size);

    for(int i = 0; i < vv.size(); i++) {
        for(int j = 0; j < vv[i].size(); j++)
            cout << vv[i][j] << " ";
        cout << endl;
    }
};