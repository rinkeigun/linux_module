/*
	2016.06.08 Huiqun.Lin
	struct型のサイズ検証
*/
#include <stdio.h>

void main()
{
	struct {
		char c1 ;
	} s1 ;
	struct  {
		char c1 ;
		char c2 ;
	} s2;
	struct  {
		char c1 ;
		char c2 ;
		int i1 ;
	} s3 ;
	struct  {
		char c1 ;
		char c2 ;
		char c3 ;
		int i1 ;
	} s4 ;
	struct  {
		char c1 ;
		char c2 ;
		double d1 ;
	} s5 ;
	struct  {
		char c1 ;
		char c2 ;
		int i1 ;
		char c3 ;
	} s6 ;
	struct {
		char c[1] ;
		char c2[4] ;
	} s7 ;
	printf("sizeof types\n") ;
	printf("sizeof struct char 1 = %d\n", sizeof ( s1 ) );
		// 結果：1
	printf("sizeof struct char 1 = %d\n", sizeof ( s2 ) );
		// 結果：2
	printf("sizeof struct char 1 = %d\n", sizeof ( s3 ) );
		// 結果：8, intと一緒に使うと、charは 4の倍数でとられる
	printf("sizeof struct char 1 = %d\n", sizeof ( s4 ) );
		// 結果：8, 4以下であれば、charを増やしてもサイズが変わりません
	printf("sizeof struct char 1 = %d\n", sizeof ( s5 ) );
		// 結果：12, doubleと一緒でも4の倍数しかとらない
	printf("sizeof struct char 1 = %d\n", sizeof ( s6 ) );
		// 結果：12, int の後にあるとやはり4byteがとられる
	printf("sizeof struct char 1 = %d\n", sizeof ( s7 ) );
		// 結果：5

}
