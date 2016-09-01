#include <iostream>
#include <fstream>

using namespace std;

int main(){
    char buf[512];

    // ifstreamのインスタンスを作る
    // C言語のfopenと同じ
    ifstream ifs( "input.txt" ) ;

    // ofstreamのインスタンスを作る
    // C言語のfopenと同じ
    ofstream ofs( "output.txt" ) ;

    // ifstreamのインスタンス(ifs)から１行読み込みbufに入れる。
    while( ifs.getline( buf, sizeof(buf) ))
        // ofstreamのインスタンス(ofs)を利用して読み込んだ内容を書き込む
        ofs << buf << endl;
}
