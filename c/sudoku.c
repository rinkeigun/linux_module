#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

typedef struct oneCell
{
	int value ;
} oneCell_t ;
void output_99( oneCell_t cells[3][3][3][3] );
void inputNumber( int num_a[3] ) ;
void set_99( oneCell_t cells[3][3][3][3], int num_a[3] ) ;
int ajudgeEndding( oneCell_t cells[3][3][3][3] );
/*
	ret : 0 終了
	      1 未完, 0を含む
	      2 不整合, 数字が重複
*/
bool check0( oneCell_t cells[3][3][3][3] ) ;
/*
	ret : true  0を含む
	      false 0を含まない
*/
bool checkSameNumber( oneCell_t cells[3][3][3][3] ) ;
/*
	ret : true  不正(重複)番号を含む
	      false 不正(重複)番号を含まない
*/


int main( int argc, char **argv )
{
	/*
		Cell[Y][X][y][x]
		Y:行
		X:列
		y:行
		x:列
	*/
	oneCell_t cell[3][3][3][3] ;
	int num_a[3] ;
	memset( cell, '\0', sizeof(cell) ) ;
	while(1)
	{
		output_99 ( cell ) ;
		inputNumber( num_a ) ;
		set_99( cell, num_a ) ;
		if( ajudgeEndding( cell ) == 0 ) break ;
	}

		
}

/*
	I : cells
*/
void output_99( oneCell_t cells[3][3][3][3] )
{
	int i=0, j= 0;
	int X, Y, x, y ;

	for(i=0; i<9; i++) // 行操作
	{
		Y = (int)(i/3) ;
		y = (i%3) ;
		for( j=0; j<9; j++) // 列操作
		{
			X = (int)(j/3) ;
			x = (j%3) ;
			printf( "%d ", cells[Y][X][y][x].value ) ;
		}
		printf("\n") ;
	}
}
void inputNumber( int num_a[3] ) 
{
	char tmp_c[256] ;
	int i = 0,j=0 ;
	gets ( tmp_c ) ;
	while( i<3 && (tmp_c[j]!='\n') ) // 行末まで
	{
		if( isdigit( tmp_c[j] ) ) 
		{
			num_a[i] = atoi(tmp_c[j]) ;
			i++ ;
		}
		j++;
	}
	
}
void set_99( oneCell_t cells[3][3][3][3], int num_a[3] ) 
{
		div_t Yy = div( num_a[0], 3) ;  // 行操作
		div_t Xx = div( num_a[1], 3) ;  // 列操作
		cells[Yy.quot][Xx.quot][Yy.rem][Xx.rem].value = num_a[2] ;
}
int ajudgeEndding( oneCell_t cells[3][3][3][3] )
{
	if( check0( cells ) == true ) return 1 ;
	if( checkSameNumber( cells ) == true ) return 2 ;
	return 0 ;
}
bool check0( oneCell_t cells[3][3][3][3] )
{
	int i=0, j=0 ;
	int X, Y, x, y ;

	for(i=0; i<9; i++) // 行操作
	{
		Y = (int)(i/3) ;
		y = (i%3) ;
		for( j=0; j<9; j++) // 列操作
		{
			X = (int)(j/3) ;
			x = (j%3) ;
			if(cells[Y][X][y][x].value == 0 ) return true ;
		}
	}
	return false ; // 0を含まない
}

bool checkSameNumber( oneCell_t cells[3][3][3][3] )
{
	int i=0, j=0 ;
	int X, Y, x, y ;

	for(i=0; i<9; i++) // 行操作
	{
		div_t Yy = div(i, 3);
		//Y = (int)(i/3) ;
		//y = (i%3) ;
		for( j=0; j<9; j++) // 列操作
		{
			div_t Xx = div( j, 3) ;
			//X = (int)(j/3) ;
			//x = (j%3) ;
			//if(cells[Y][X][y][x].value == 0 ) return true ;
			if(cells[Yy.quot][Xx.quot][Yy.rem][Xx.rem].value == 0 ) return true ;
		}
	}
	return false ; // 0を含まない
}
