#include <stdarg.h>

/* 可変引数である関数を定義 */
/*(指定された不定引数を全て表示する関数)*/
void vararg_func( char * argv , ... ) {
  va_list list;/* 定義するだけで値は設定しない */
  int i;
  char * cp;

  /* ①可変引数にアクセスする前の初期処理 */
  /* 第２引数に指定するargcは、vararg_func引数"..."の
                            直ぐ左側でなければならない*/
  va_start( list ,  argv );

  /* cpの文字列の長さが引数個数を意味し
     文字列の各文字がデータ型を意味する */
  for( cp=( char * )argv , i=0 ; *cp != '\0'
                              ; cp++ , i++ ) {
    if( *cp == 's' ) { /* char*型 */
      /* ②可変引数にアクセスしてその変数を取り出す処理 */
      /* 第２引数にchar*型を指定 */
      printf( "argv(%d)=%s\n" , i
                   , va_arg( list , char * ));
    }
    else
    if( *cp == 'c' ) { /* char型 */
      /* ②可変引数にアクセスしてその変数を取り出す処理 */
      /* 第２引数にchar型を指定したい時は
                    int型を指定した上でchar型にcastする */
      printf( "argv(%d)=%c\n" , i
                   , ( char )va_arg( list , int ));
    }
    else
    if( *cp == 'd' ) { /* int型 */
      /* ②可変引数にアクセスしてその変数を取り出す処理 */
      /* 第２引数にint型を指定 */
      printf( "argv(%d)=%d\n" , i
                   , va_arg( list , int ));
    }
  }

  /* ③可変引数にアクセスした後の終了処理 */
  va_end( list );
}

/* メイン関数 */
main() {
  /* 不定引数の加算関数を呼び出す */
  /* "scd":各々String , Char , Intを意味し
                      文字列の長さがデータ個数を意味する */
  vararg_func( "scd" , "abc" , 'd' , 123 );
}
