/*
	2016/06/17	Huiqun.Lin
	ヒープ領域が下位へ広げ、スタック領域が上位へ広げる様子を見る
	出力結果
	-----------------------------------------------------------
	heap = 0x9518008 : stack = 0xbfec2e48
	heap = 0x9518018 : stack = 0xbfec2e18
	....................................
	heap = 0x97c2198 : stack = 0xbf6c4998
	heap = 0x97c21a8 : stack = 0xbf6c496
	Segmentation fault
	-----------------------------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>

void func(void)
{
  int b = 4 ;  /* スタック領域追加 */
  int *a ;
  a = malloc(sizeof(int)); /* ヒープ領域追加 */

  printf("heap = %p : stack = %p\n",a,&b);
  func();
}

int main(void)
{

  func();

  return(0);
}
	

