/*
	2016.06.15 Huiqun.Lin
	出力検証
*/

#include <stdio.h>
#include <stdbool.h>

int main( int argc, char **args )
{

	int		a = 12, b = 58;
	char	str1[] = "Hello";
	char	str2[] = "world";
	int		data = 123;
	double	x = 654.321;
		
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
	printf("%% [フラグ][フィールド幅][.精度][変換指定文字]\n" ) ;
	printf("[フラグ]\n" ) ;
	printf("- : 左詰めに表示する（省略時には右詰め）\n" ) ;
	printf("+ : 符号を付ける（省略時には \"-\" 符号のみ）\n" ) ;
	printf("# : 数値の表記形式がわかるように表示する\n") ;
	printf("右詰め：%10s%10s\n", str1, str2);
	printf("左詰め：%-10s%-10s\n", str1, str2);
	printf("符号あり：%+d\n", a);
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

	printf("[変換指定文字]\n" ) ;
	printf("diouxXfeEgGcs\n" ) ;
	printf("d : %d\n" , 1 ) ;
	printf("i : %i\n" , 1 ) ;
	printf("o : %#o\n" , 1 ) ;
	printf("u : %u\n" , 1 ) ;
	printf("x : %#x\n" , 1 ) ;
	printf("X : %#X\n" , 1 ) ;
	printf("f : %f\n" , 1.04 ) ;
	printf("e : %e\n" , 10000.5 ) ;
	printf("E : %E\n" , 10000.1 ) ;
	printf("g : %g\n" , 1.2 ) ;
	printf("G : %G\n" , 1.33 ) ;
	printf("c : %c\n" , 91 ) ;
	printf("s : %s\n" , "文字列" ) ;

	return 0 ;
	
}
