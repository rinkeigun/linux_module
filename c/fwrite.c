#include <stdio.h>
#include <string.h>
#include <errno.h>


void main()
{
	char *filePath = "./sd//log/fwrite/test.txt" ;
	char *data = "abcde" ;
	int size = strlen ( data ), ret ;
	FILE *fp ;

	fp = fopen( filePath, "ab" );
	printf("filePath( %s )\n", filePath ) ;
	ret = fwrite( data, 1, size, fp );
	printf("ret = %d\n", ret ) ;
	if( ret < 1 )
	{
		printf("error( %d:%s )\n", errno, strerror( errno ) ) ;
	}
	fclose( fp );
}
