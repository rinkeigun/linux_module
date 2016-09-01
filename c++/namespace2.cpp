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

// これ以下は、Tokyo::と付けなくても、暗黙でYamadaだけはTokyoを調べてくれる
using Tokyo::Yamada;

int main(){
    // 今回は、TokyoのPrintNameは見えておらず、グローバルなPrintNameのみ見えているので
    // YamadaはTokyo::を見てくれる
    // OK
    PrintName(Yamada);

    // TokyoのPrintNameを呼ぼうとしている
    // これはOK
    Tokyo::PrintName(Tokyo::Yamada);

    // グローバルなPrintNameを呼ぼうとしている
    // YamadaはTokyo::を見てくれる
    // これもOK
    ::PrintName(Yamada);
}
