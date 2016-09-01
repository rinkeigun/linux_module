#include <stdio.h>

void main()
{
	int wd2mMagTmp = 0 ;
	int i ;

	for( i = 0; i<360; i++)
	{
		wd2mMagTmp = i ;

    	if( wd2mMagTmp>=1 && wd2mMagTmp<=4 )           { wd2mMagTmp = 360; }
    	else if( wd2mMagTmp%10>=1 && wd2mMagTmp%10<=4) { wd2mMagTmp = wd2mMagTmp    - wd2mMagTmp%10; }
    	else if( wd2mMagTmp%10>=5 && wd2mMagTmp%10<=9) { wd2mMagTmp = wd2mMagTmp+10 - wd2mMagTmp%10; }
		printf("%d:%d\n", i, wd2mMagTmp ) ;
	}
}
