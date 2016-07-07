/*
	2016.06.08 Huiqun.Lin
	bool 型のサイズ、値を検証
*/
#include <stdio.h>
#include <stdbool.h>

void main()
{
	bool a = true ;
	bool b = false ;

	bool c = 2 ;
	bool d = 3 ;
	bool e = -2 ;

	short int g, h, i ;

	printf("a=%d, b=%d, c=%d, d=%d, e=%d\n", a, b, c, d, e ) ;
	printf("size a=%d, b=%d, c=%d, d=%d, e=%d bool=%d, char=%d\n", 
		sizeof(a), 
		sizeof(b), 
		sizeof(c), 
		sizeof(d), 
		sizeof(e),
		sizeof(bool), 
		sizeof(char) ) ;

  g = 11;
  h = 14;

  printf("%#x(%d) AND %#x(%d) = %#x(%d)\n", g,g, h,h, g & h, g&h);
  printf("%#x(%d) OR  %#x(%d) = %#x(%d)\n", g,g, h,h, g | h,g|h);
  printf("%#x(%d) XOR %#x(%d) = %#x(%d)\n", g,g, h,h, g ^ h,g^h);
  printf("NOT %#x(%d) = %#x(%d)\n", g,g, ~g, ~g);
for( i=0; i<4; i++)
{
  printf("%#x = %d << %d\n", 1<<i, 1, i);
}
  printf("%#x = %d >> %d\n", 7>>1, 7, 1);

}
