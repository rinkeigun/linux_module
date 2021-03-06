#include<iostream>

using namespace std;

namespace Tokyo{
    const char* Yamada = "Yamada Taro";

    // TokyoのPrintName関数
    void PrintName(const char* name){
        cout << name << endl;
    }
}

// グローバルなPrintName
void PrintName(const char* name){
        cout << name << "  " << name << endl;
}

// これ以下は、Tokyo::と付けなくても、暗黙でTokyoを調べてくれる
using namespace Tokyo;

int main(){
    // さっきはどこのYamadaさんだかわからなかったが、今回はTokyoのYamadaさんだとわかる
    // しかし、PrintNameがTokyoのPrintNameだか、グローバルなPrintNameだかわからないので
    // エラー
    //PrintName(Yamada);

    // TokyoのPrintNameを呼ぼうとしている
    // これはOK
    Tokyo::PrintName(Tokyo::Yamada);

    // グローバルなPrintNameを呼ぼうとしている
    // これもOK
    ::PrintName("Suzuki");
}
