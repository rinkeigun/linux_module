#include <stdio.h>

void f( int *a )
{
	*a += 1 ;
}

void fname()
{
	int fname = 0 ;
		f( &fname ) ;
		printf("<%d>", fname) ;
		fflush(stdout) ;
}


void main()
{
	while(1){
		fname();
		sleep( 1 ) ;
	}
}
