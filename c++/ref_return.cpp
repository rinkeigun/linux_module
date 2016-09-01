#include <iostream>

using namespace std;

int& func(){
    static int i = 10;
    return i;
}

int main(){
    cout << ++func() << endl;
    cout << func()++ << endl;
    cout << func()++ << endl;
}

