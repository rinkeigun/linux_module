#include <stdio.h>

// a : 変数, b 
#define bitget(v,n)		((v) >> (n)) & 1
#define bitset(v,n)		(v) |= (1 << (n))
#define bitunset(v,n)	(v) &= ~(1 << (n))
#define min(a,b)		(a)<(b) ? (a) : (b)
#define max(a,b)		(a)>(b) ? (a) : (b)
#define ope(a,b,i)		(a)<(b) ? ((i)++) : ((i)--)

int print_bit( v, start_no, end_no )
char *v;		// I  : ビット出力対象変数
int start_no;	// I  : 出力開始位置, 普通はend_noより大きい値を指定 
int end_no;		// I  : 出力終了位置 
{
	int i = start_no ;
	
	while(1)
	{
        printf("%d", bitget(*v, i));
		if( i == end_no ) break ;
		ope( start_no, end_no, i ) ;
	}
}

void bit_H2L_8(v, start_no)
char *v ;		//I  : ビット出力対象変数
int	 start_no ;	//I  : 出力ビット開始位置 
{
	print_bit( v, start_no,  start_no - 7 ) ;
}

void bit_L2H_8(v, start_no)
char *v ;		//I  : ビット出力対象変数
int	 start_no ;	//I  : 出力ビット開始位置 
{
	print_bit( v, start_no,  start_no + 7 ) ;
}

void print_hyphen_8()
{
	printf( "--------" ) ;
}

void main()
{
	int a = 15 ;
	bit_H2L_8( &a,  7) ;
	printf("\n") ;
	bit_L2H_8( &a,  0) ;
	printf("\n") ;
	print_hyphen_8() ;
}
