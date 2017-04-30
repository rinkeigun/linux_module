#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define INT int
#define MAX( a, b )  (a)>(b)?(a):(b)
#define SQRT2( a, b ) ((INT)sqrt( (a)*(a)+(b)*(b) ))
#define SQRT3( a, b, c ) ((INT)sqrt( (a)*(a)+(b)*(b)+(c)*(c) ))

bool call3( INT a, INT b, INT c, INT *d )
{
	INT s = SQRT3( a, b, c ) ;
	*d = 0 ;
	

	//for(INT cnt = MAX( MAX( a, b ), c ); cnt < a+b+c; cnt ++)
	for(INT cnt = s; cnt < s+2; cnt ++)
	{
		if( (cnt*cnt) == ( a*a + b*b + c*c ) )
		{
			*d = cnt;
			return true ;
		}
	}
	return false ;
}
bool call2( INT a, INT b, INT *d ) 
{
	INT s = SQRT2( a, b ) ;
	*d = 0 ;

	//for( INT cnt = MAX(a, b); cnt < a+b; cnt ++)
	for( INT cnt = s; cnt < s+2; cnt ++)
	{
		//printf("\t cnt=%d\n", cnt) ;
		if( (cnt * cnt) == ( a * a + b * b ) )
		{
			*d = cnt ;
			return true ;
		}
		
	}
	return false; 
}
	

int main(int argc, char *argv[])
{
	
	INT x=3, y, z ;
	INT xy, yz, zx, xyz ;
	//INT cnt_y, cnt_z ;
	bool xy_flg= true, yz_flg= true, zx_flg= true, xyz_flg = true;
	int cnt4 = 0;

	x = atol( argv[1] ) ;
//printf( "x = %d\n", x ) ;
//printf( "int 0.4, 0.5 = %d, %d\n", (INT)0.4, (INT)0.5 ) ;

	while(1)
	//while(x<6)
	{
		for( y = 2; y < x ; y ++)
		{
			for( z = 1; z < y ; z ++)
			{
				//printf("1. x=%d, y=%d, z=%d\n", x, y, z);
				
				xy_flg = call2( x, y , &xy) ;
				yz_flg = call2( y, z , &yz) ;
				zx_flg = call2( z, x , &zx) ;
				xyz_flg = call3( x, y, z , &xyz) ;
				
				if( xy_flg && yz_flg && zx_flg && xyz_flg ) break ;
				cnt4=	(xy_flg? 1:0)+
					(yz_flg? 1:0)+
					(zx_flg? 1:0)+
					(xyz_flg ? 1:0)  ;
				//if( xy_flg || yz_flg || zx_flg || xyz_flg )
				if( cnt4 >2 )
				printf("x=%d, y=%d, z=%d, xy=%d, yz=%d, zx=%d, xyz=%d\n",
					x, y, z,

					xy_flg? xy:0,
					yz_flg? yz:0,
					zx_flg? zx:0,
					xyz_flg ? xyz:0 ) ;
			}
		}
		printf("x=%d\n", x) ;
		x ++ ;
	}
	return true;
	
}
