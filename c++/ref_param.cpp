#include <iostream>

using namespace std;

void func(int& n){
    n++;
}

int main(){
    int i = 10;
    func(i);

    cout << i << endl;
}

