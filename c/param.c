#include <stdio.h>

void cal_a( int a, int *b )
{
	a = 2 ;
	*b = 2 ;
}
void main()
{
	int a = 0 ;
	int b = 0 ;

	cal_a( a, &b ) ;

	printf("a = %d, b=%d\n", a, b ) ;
}
