/*
	2016.06.08 Huiqun.Lin
	負数、小数のbit表現の検証
*/

#include <stdio.h>
#include <limits.h>
#include <float.h>

void main()
{
	char c_min = -128 ;		// 10000000
	char c_min1 = -1 ;		// 11111111
	char c_0 = 0 ;			// 00000000
	char c_p1 = 1 ;			// 00000001
	char c_max = 127 ;		// 01111111

	float f_p1 = 0.1 ;	
	float f_p2 = 1.0 ;	
	float f_p3 = 0.0 ;	
	float f_p4 = 1.1 ;	

	float fm_p1 = -0.1 ;
	float fm_p2 = -1.0 ;	
	float fm_p3 = -0.0 ;	
	float fm_p4 = -1.1 ;	

	printf( "どんな結果になるか" ) ;

}
