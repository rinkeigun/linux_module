#include <stdio.h>

void main()
{
	int i=21 ;

	while(1)
	{
		if( (i%5==1) &&
			(i%6==3) &&
			(i%7==0) &&
			(i%8==1) &&
			(i%9==0) ) break ;
		i++;
	}
	printf( "i=%d\n", i ) ;
}
