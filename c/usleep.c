#include <stdio.h>
#include <unistd.h>

void main()
{
	int i = 0 ;

	while( i<10)
	{
		usleep( 1000000 ) ;    // １秒
		printf("%d\n", ++i) ;
	}
}
