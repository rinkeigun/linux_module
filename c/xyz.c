#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define INT long long unsigned
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
		//printf("\t cnt=%llu\n", cnt) ;
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
	//printf( "x = %llu\n", x ) ;
	//printf( "int 0.4, 0.5 = %llu, %llu\n", (INT)0.4, (INT)0.5 ) ;

	while(1)
	//while(x<6)
	{
		for( y = 2; y < x ; y ++)
		{
				xy_flg = call2( x, y , &xy) ;
				if( !xy_flg ) continue ;
				//else printf("xy=%llu, ", xy ) ;
			for( z = 1; z < y ; z ++)
			{
				//printf("\n x=%llu, y=%llu, z=%llu, ", x, y, z);
				
				yz_flg = call2( y, z , &yz) ;
				if( !yz_flg ) continue ;
				//else printf("yz=%llu, ", yz ) ;
				zx_flg = call2( z, x , &zx) ;
				if( !zx_flg ) continue ;
				//else printf("zx=%llu, ", zx ) ;
				xyz_flg = call3( x, y, z , &xyz) ;
				
				if( xy_flg && yz_flg && zx_flg && xyz_flg ) 
				{
					printf("x=%llu, y=%llu, z=%llu, xy=%llu, yz=%llu, zx=%llu, xyz=%llu\n",
					x, y, z,
					xy_flg? xy:0,
					yz_flg? yz:0,
					zx_flg? zx:0,
					xyz_flg ? xyz:0 ) ;
					return true ;
				}
				cnt4=	(xy_flg? 1:0)+
					(yz_flg? 1:0)+
					(zx_flg? 1:0)+
					(xyz_flg ? 1:0)  ;
				if( cnt4 >2 )
				printf("x=%llu, y=%llu, z=%llu, \x1b[46mxy=%llu, yz=%llu, zx=%llu, xyz=%llu\x1b[0m\n",
					x, y, z,
					xy_flg? xy:0,
					yz_flg? yz:0,
					zx_flg? zx:0,
					xyz_flg ? xyz:0 ) ;
			}
		}
		if( x%100 == 0 ) printf("x=%llu\n", x) ;
		x ++ ;
	}
	return true;
	
}
