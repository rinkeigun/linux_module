#include <stdio.h>

#define ope( i, a, b )	(b)>(a)? (i)++ : (i)--
//#define ope2(  a, b )	(b)>(a)? ++ : --

void main()
{
	int i = 0 ;
	int a = 3, b = 4 ;

	ope( i, a, b ) ;
	printf( "a < b, i = %d\n", i ) ;

	a =  4; 
	b = 3 ;
	ope( i, a, b ) ;

	printf( " a > b, i = %d\n", i ) ;

/*
	i ope2( a , b ) ;
	
	printf( " a > b, i = %d\n", i ) ;
*/
	
}
