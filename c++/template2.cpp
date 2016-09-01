/*
// add(int, int), add(double, double)に化けてくれるが、
// add(int, char)のように異なる型には化けてくれない。
// 異なる型にも化けさせるには、下のようなテンプレートにしなければいけない
template<class Type>
Type add(Type arg1, Type arg2){
    return arg1 + arg2;
}
*/

// 加算2(テンプレート版)
template<class Type1, class Type2>
Type1 add(Type1 arg1, Type2 arg2){
    return arg1 + arg2;
}

#include<iostream>
using namespace std;

int main(){
    int n1 = 10, n2 = 20, n3;

    n3 = add(n1, n2);
    cout << n3 << endl;

    char ch = 1;
    // 加算2が呼ばれる
    n3 = add(n1, ch);
    cout << n3 << endl;
}
