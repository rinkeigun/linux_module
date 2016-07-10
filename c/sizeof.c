/*
	2016.06.08 Huiqun.Lin
	各種データ型のサイズ検証
*/
#include <stdio.h>
#include <stdbool.h>

char cf()
{
	return 'c' ;
}
int if1()
{
	return 1 ;
}
double df()
{
	return 3.14 ;
}
double *dfp()
{
	double pi = 3.14 ;
	return &pi ;
}

void main()
{
	union 
	{
		char c ;
		int  i ;
		double d ;
	} u ;
	int *ip ;
	char *cp ;
	double *dp ;

	printf("sizeof types\n") ;
	printf("sizeof bool = %d\n", sizeof ( bool ) );
		// 結果：1
	printf("sizeof char = %d\n", sizeof ( char ) );
		// 結果：1
	printf("sizeof unsigned char = %d\n", sizeof ( unsigned char ) );
		// 結果：1
	printf("sizeof int = %d\n", sizeof ( int ) );
		// 結果：4
	printf("sizeof short int = %d\n", sizeof ( short int ) );
		// 結果：2
	printf("sizeof long int = %d\n", sizeof ( long int ) );
		// 結果：4
	printf("sizeof float = %d\n", sizeof ( float ) );
		// 結果：4
	printf("sizeof double = %d\n", sizeof ( double ) );
	printf("sizeof double long = %d\n", sizeof ( double long ) );
		// 結果：8
	printf("sizeof long double = %d\n", sizeof ( long double ) );
		// 結果：12
	printf("sizeof struct = %d\n", sizeof ( struct s{ char c; int i; }   ) );
		// 結果：8, 構造体内部にはcharはサイズが 4 をとる。これについては別途struct sizeofで検証
	printf("sizeof pointer union = %d\n", sizeof ( u ) );
		// 結果：8, 最大サイズのdoubleサイズをとる
	printf("sizeof enum = %d\n", sizeof ( enum e_tag{EA, EB }  ) );
		// 結果：4
	printf("sizeof pointer *char = %d\n", sizeof ( cp ) );
	printf("sizeof pointer *int = %d\n", sizeof ( ip ) );
	printf("sizeof pointer *double = %d\n", sizeof ( dp)  );
		// 結果：すべて4
	printf("sizeof pointer *function = %d\n", sizeof ( dfp)  );
		// 結果：1
	printf("sizeof char function = %d\n", sizeof ( cf  ) );
	printf("sizeof int function = %d\n", sizeof ( if1  ) );
	printf("sizeof double function = %d\n", sizeof ( df  ) );
		// 結果：すべて1

}
