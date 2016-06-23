#include <stdio.h>

void func1( int a )
{
	int i ;

	for( i = 0; i<a ; i++)
	{
		if( i%2 == 0 )
		{
			printf( "test\n" ) ;
		}
		else {
			printf( "test1\n" ) ;
		}
	}
}

void main()
{
	int j = 5 ;
	func1( j ) ;
}
