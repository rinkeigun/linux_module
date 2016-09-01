// 絶対値を求める(テンプレート版)
template<class Type>
Type abs(Type arg){
    return (arg < 0) ? -arg : arg;
}

#include<iostream>
using namespace std;

int main(){
    int n = -10;
    n = abs(n);
    cout << n << endl;

    double d = -10;
    d = abs(d);
    cout << d << endl;
}


