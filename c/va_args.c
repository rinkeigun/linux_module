#include <stdio.h>

#define va_args( fmt, ... ) printf("%s:%d " fmt "\n", __FUNCTION__, __LINE__, __VA_ARGS__ )
/* 
arm
#define va_args( fmt, ... ) printf("%s:%d " fmt "\n", __FUNCTION__, ##__LINE__, __VA_ARGS__ )
*/
void main()
{
	va_args( " %d ", 123 ) ;
}
