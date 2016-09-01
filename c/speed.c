#include <stdio.h>

void check_include( int i, int max, int min, int mean );
void main()
{
	int i, max, min, mean ;
	
	printf("間\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 7, 2, 4 ) ;
	}
	printf("奇数\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 11, 11, 11 ) ;
	}
	printf("偶数\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 12, 12, 12 ) ;
	}
	printf("MIN\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 17, 12, 12 ) ;
	}
	printf("MAX\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 17, 12, 17 ) ;
	}
	printf("same0\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 0, 0, 0 ) ;
	}
	printf("0\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 5, 0, 0 ) ;
	}
	printf("same60\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 60, 60, 60 ) ;
	}
	printf("60\n") ;
	for(i=0; i<31; i++)
	{
		check_include(i, 60, 0, 60 ) ;
	}
}

void check_include( int i, int max, int min, int mean )
{
	int dv = 2 ;
	int speed = i * dv ;
	int speed1 = (speed == 0) ? 0 : (speed - 1) ;

    if ((max >= speed && min <= speed)||(max >=speed1&&min<=speed1))
    {
		if (mean <= speed && mean > speed - dv)
		{
			printf("%d:%d,%d,%d-%d (Green)\n",i, max, mean, min, speed);
		}
		else
		{
			printf("%d:%d,%d,%d-%d (LightGreen)\n",i, max, mean, min, speed);
		}
	}
	else
	{
		printf("%d:%d,%d,%d-%d (BackColor)\n",i, max, mean, min, speed);
	}
}
