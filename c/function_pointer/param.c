#include <stdarg.h>

/* 可変引数である関数を定義 */
/*(指定された不定引数を全て加算する関数)*/
void vararg_func( int * sum , int argc , ... ) {
  va_list list;/* 定義するだけで値は設定しない */
  int i;

  *sum = 0;/* 加算結果をクリア */

  /* ①可変引数にアクセスする前の初期処理 */
  /* 第２引数に指定するargcは、vararg_func引数"..."の
                            直ぐ左側でなければならない*/
  /*(直ぐ左側→sumとargcを入れ替えると
                            コンパイルエラーになる)*/
  va_start( list ,  argc );

  for( i=0 ; i<argc ; i++ ) {
    /* ②可変引数にアクセスしてその変数を取り出す処理 */
    /* 第２引数にint型を固定指定 */
    *sum += va_arg( list , int );
  }

  /* ③可変引数にアクセスした後の終了処理 */
  va_end( list );
}

/* メイン関数 */
main() {
  int argv[3];
  int i , argc , sum;

  /* データ件数を求める */
  argc = sizeof( argv )/sizeof( argv[0] );

  /* データを設定 */
  for( i=0 ; i<argc ; i++ ) {
    argv[i] = i + 1;
  }

  /* 不定引数の加算関数を呼び出す */
  /*(sumを指定して結果を得ることも可能)*/
  vararg_func( &sum , argc , argv[0] , argv[1] , argv[2] );

  /* 加算結果を出力 */
  printf( "sum=%d\n" , sum );/* 6 */
}
