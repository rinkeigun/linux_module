/*
	2016/06/17	Huiqun.Lin
	overflow検証
	出力：Hello Over Flow!!
*/

#include <stdio.h>
#include <stdlib.h>

int i ;

void sub(void)
{
	printf("Hello Over Flow!!\n");
	exit(0);
}  /* 呼び出す予定がない関数 */

void func(void)
{
  //int i ; 
	// iを関数内部から移出、
	//関数内だとメモリ上aの後ろに配置されstackoverを起こす前、
	// iの値が変化し、大きな値が代入される可能性があり、forループが終了してしまう。
  int a[1];
  for ( i = 0 ; i < 3 ; i++ )
  {
    a[i] = (int)sub ;  /* 配列aに関数sub()のアドレスを代入 */
  }
}

int main(void)
{
	func();
	return(0);
}
