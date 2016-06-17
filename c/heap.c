/*
	2016/06/17	Huiqun.Lin
	ヒープ領域とスタック領域の違いを見る 
	出力：program = 0x804841d : heap = 0x804a020 : stack = 0xbfe5f9dc
*/

#include <stdio.h>

int a = 4 ;

void func(void)
{
  int b = 2 ;
  printf("program = %p : heap = %p : stack = %p\n",func,&a,&b);
}

int main(void)
{

  func();

  return(0);
}
	
