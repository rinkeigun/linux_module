#include <stdio.h>
#include <stdbool.h>

void main()
{
	bool a = true ;
	bool b = false ;

	bool c = 2 ;
	bool d = 3 ;
	bool e = -2 ;

	printf("a=%d, b=%d, c=%d, d=%d, e=%d\n", a, b, c, d, e ) ;
	printf("size a=%d, b=%d, c=%d, d=%d, e=%d bool=%d\n", 
		sizeof(a), 
		sizeof(b), 
		sizeof(c), 
		sizeof(d), 
		sizeof(e),
		sizeof(bool) ) ;
}
