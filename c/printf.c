/*
	2016.06.15 Huiqun.Lin
	出力検証
*/

#include <stdio.h>
#include <stdbool.h>

int main( int argc, char **args )
{

	int		a = 1223, b = 58;
	char	str1[] = "Hello";
	char	str2[] = "world";
	int		data = 123;
	double	x = 654.321;

	char *fmt = "引数順は　%2$s を　%1$s に指定できる\n\n" ;
	char *cmd = "cmd" ;
	char *first = "1" ;

		
	printf("bool : TRUE %c, FALSE %c\n", true, false ) ;
/*
       \"     double quote
       \\     backslash
       \a     alert (BEL)
       \b     backspace
       \c     produce no further output
       \e     escape
       \f     form feed
       \n     new line
       \r     carriage return
       \t     horizontal tab
       \v     vertical tab
       \NNN   byte with octal value NNN (1 to 3 digits)
       \xHH   byte with hexadecimal value HH (1 to 2 digits)
       \uHHHH Unicode (ISO/IEC 10646) character with hex value HHHH (4 digits)
       \UHHHHHHHH
              Unicode character with hex value HHHHHHHH (8 digits)
       %%     a single %
       %b     ARGUMENT  as  a string with '\' escapes interpreted, except that
              octal escapes are of the form \0 or \0NNN
*/
	printf("%% [引数順][フラグ][フィールド幅][.精度][長さ修飾子][変換指定文字]\n\n" ) ;
	printf( fmt, first, cmd ) ;
	printf("[フラグ]\n\n" ) ;
	printf("- : 左詰めに表示する（省略時には右詰め）\n" ) ;
	printf("+ : 符号を付ける（省略時には \"-\" 符号のみ）\n" ) ;
	printf("(空白)+ : 符号を付ける（省略時には \"-\" 符号のみ）\n" ) ;
	printf("# : 数値の表記形式がわかるように表示する\n") ;
	printf("0 : 左を0で詰める \n") ;
	//printf("\, : 三桁に,を入れる \n") ;
	printf("右詰め：%10s%10s\n", str1, str2);
	printf("左詰め：%-10s%-10s\n", str1, str2);
	printf("符号あり：%+d\n", a);
	printf("空白：% d\n", a);
	printf("0：%0d\n", a);
	//printf("\,：%,d\n", a);
	printf(" 8進表示：%#o\n", b);
	printf("16進表示：%#x\n", b);

	printf("[フィールド幅]\n" ) ;
	printf("%d\n", data);
	printf("%5d -> スペース含めて 5文字\n", data);
	printf("%10d -> スペース含めて 10文字\n", data);
	printf("%2d ->  指定が小さい場合は必要幅\n", data);
	printf("%05d -> 0フラグがあると0を詰める\n", data);

	printf("[.精度]\n" ) ;
	printf("%f\n", x);
	printf("%12f -> 小数点を入れて 12桁（小数点以下の桁は標準値）\n", x);
	printf("%9.2f -> 小数点を入れて 9桁（小数点以下 2桁）\n", x);

	printf("[長さ修飾子]\n" ) ;

	printf("hh 実引数は char 型 C99以降 \n" ) ;
	printf("h 実引数は short 型 全バージョン \n" ) ;
	printf("l（エル） 実引数は long 型または wchar_t 型または double 型[1] wchar_t についてはC95以降、double についてはC99以降 \n" ) ;
	printf("ll（エルエル） 実引数は long long 型 C99以降 \n" ) ;
	printf("j 実引数は intmax_t 型 C99以降 \n" ) ;
	printf("z 実引数は size_t 型 C99以降 \n" ) ;
	printf("t 実引数は ptrdiff_t 型 C99以降 \n" ) ;
	printf("L 実引数は long double 型 全バージョン \n" ) ;
	printf(" 実引数は char16_t 型  \n" ) ;
	printf(" 実引数は char32_t 型 \n" ) ;

	printf("[変換指定文字]\n" ) ;
	printf("adiouxXfeEgGcs\n" ) ;
	printf("a : %a <- 16進浮動小数点\n" , 3.14 ) ;
	printf("A : %A <- 16進浮動小数点\n" , 1.44 ) ;
	printf("d : %d <- 10進符号付き整数\n" , 1 ) ;
	printf("i : %i <- 10進符号付き整数\n" , 1 ) ;
	printf("o : %#o <- 8進符号無し整数\n" , 1 ) ;
	printf("u : %u <- 10進符号無し整数\n" , 1 ) ;
	printf("x : %#x <- 16進符号無し整数\n" , 1 ) ;
	printf("X : %#X <- 16進符号無し整数\n" , 1 ) ;
	printf("f : %f\n" , 1.04 ) ;
	printf("e : %e\n" , 10000.5 ) ;
	printf("E : %E\n" , 10000.1 ) ;
	printf("g : %g\n" , 1.2 ) ;
	printf("G : %G\n" , 1.33 ) ;
	printf("c : %c\n" , 91 ) ;
	printf("s : %s\n" , "文字列" ) ;
	printf("p : %p\n" , cmd ) ;
	//printf("n : %n <- 整数変数に出力済み文字数を格納\n" , &a ) ;

	return 0 ;
	
}
