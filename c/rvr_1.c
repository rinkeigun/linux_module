/*
	2016/06/20	Huiqun.Lin
	gcc rvr_1.c -lm
*/
#include <stdio.h>
#include <math.h>

void main()
{
			const double E = 2.71828183;	// ネイピア数
			double wk1;
			double wk2;
			double MOR_up;		// RVR=550mでのMOR_550
			double MOR_low;		// RVR=200mでのMOR_200
			double a;			// 内分率α（0≦α≦1）
			double mor = 245;
			double ie = 500;
			double et = 0.0000020474;
			double ic = 250;
			double upper_limit = 550;
			double lower_limit = 200;
			double rvr_ec, rvr_1 ;
			
			// 照度閾値 E_t  、滑走路灯の灯火光度 I_e   を用いて、RVR=550mでのMOR_550 を算出する
			//double log_e = log( E ) ;
			double log_e = 1 ;
			//double log_e = log( 2.71828183 ) ;
			wk1 = log( 1 / 0.05 ) / log_e;
			wk2 = log( ie / ( et * (upper_limit * upper_limit) ) ) / log_e;
			MOR_up = upper_limit * ( wk1 / wk2 );
	printf( "wk1:\t%f, %f, %f, ie=%f, et=%f, upper_limit=%f\n", wk1,wk2, MOR_up, ie, et, upper_limit ) ;
			
			// 照度閾値 E_t  、滑走路中心線灯の灯火光度 I_c   を用いて、RVR=200mでのMOR_200 を算出する
			wk2 = log( ic / (et * (  lower_limit * lower_limit) ) ) / log_e;
			MOR_low =  lower_limit * ( wk1 / wk2 );
			
			// MOR＝α?MOR_550+(1-α)?MOR_200 となる、内分率α（0≦α≦1）を下式のとおり算出する
			a = ( mor - MOR_low ) / ( MOR_up - MOR_low );
			
			// 仮RVRを算出する。ただし、小数第1位を四捨五入し、整数[m]とする
			rvr_ec = ( a * upper_limit ) + (( 1 - a ) * lower_limit );
			rvr_ec = round( rvr_ec );
			
			// RVR1分間平均値（RVR1）として代入
			rvr_1 = rvr_ec;
	printf( "rvr_1:\t%f\n", rvr_1 ) ;
}
