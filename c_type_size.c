/* 
	2016.06.08 Huiqun.lin
	各型の最大、最小値およびoverflowの検証
*/

#include <stdio.h>
#include <limits.h>
#include <float.h>

int main (int argc, char **argv)
{
	char	co1 = CHAR_MAX + 1 ;
	char	co2 = CHAR_MIN - 1 ;			// warning: overflow in implicit constant conversion [-Woverflow]
	signed char	sco1 = SCHAR_MAX + 1 ;
	signed char	sco2 = SCHAR_MIN - 1 ;		// warning: overflow in implicit constant conversion [-Woverflow]
	unsigned char	uco1 = UCHAR_MAX + 1 ;	// warning: large integer implicitly truncated to unsigned type [-Woverflow]
	unsigned char	uco2 = -1 ;
	int	io1 = INT_MAX + 1 ;					// warning: integer overflow in expression [-Woverflow] 
	int	io2 = INT_MIN - 1 ;					// warning: integer overflow in expression [-Woverflow] 
	unsigned int	uio1 = UINT_MAX + 1 ;
	unsigned int	uio2 = -1 ;
	long	lo1 = LONG_MAX + 1 ;			// warning: integer overflow in expression [-Woverflow] 
	long	lo2 = LONG_MIN - 1 ;			// warning: integer overflow in expression [-Woverflow] 
	unsigned long	ulo1 = ULONG_MAX + 1 ;
	unsigned long	ulo2 =  -1 ;
	float	flt1 = FLT_MAX + 1 ;
	float	flt2 = FLT_MIN - 1 ;
	double	dbl1 = DBL_MAX + 1 ;
	double	dbl2 = DBL_MIN - 1 ;	
	long double	ldbl1 = LDBL_MAX + 1 ;
	long double	ldbl2 = LDBL_MIN - 1 ;	

        printf("%s\t%d\n", "char型の最大値", CHAR_MAX);
			// CHAR_MAX : 127
        printf("%s\t%d\n", "char型の最小値", CHAR_MIN);
			// CHAR_MIN : -128
        printf("%s\t%d\n", "signed char型の最大値", SCHAR_MAX);
			// SCHAR_MAX : 127
        printf("%s\t%d\n", "signed char型の最小値", SCHAR_MIN);
			// SCHAR_MIN : -128
        printf("%s\t%d\n", "unsigned char型の最大値", UCHAR_MAX);
			// UCHAR_MAX : 255
        printf("%s\t%d\n", "short型の最大値", SHRT_MAX);
			// SHRT_MAX : 32767
        printf("%s\t%d\n", "short型の最小値", SHRT_MIN);
			// SHRT_MIN : -32768
        printf("%s\t%d\n", "unsigned short型の最大値", USHRT_MAX);
			// USHRT_MAX : 65535
        printf("%s\t%d\n", "int型の最大値", INT_MAX);
			// INT_MAX : 2147483647
        printf("%s\t%d\n", "int型の最小値", INT_MIN);
			// INT_MIN : -2147483648
        printf("%s\t%u\n", "unsigned int型の最大値", UINT_MAX);
			// UINT_MAX : 4294967295
        printf("%s\t%ld\n", "long型の最大値", LONG_MAX);
			// LONG_MAX : 2147483647
        printf("%s\t%ld\n", "long型の最小値", LONG_MIN);
			// LONG_MIN : -2147483648
        printf("%s\t%lu\n", "unsigned long型の最大値", ULONG_MAX);
			// ULONG_MAX : 4294967295
        printf("%s\t%g\n", "float型の最大値", FLT_MAX);
			// FLT_MAX : 3.40282e+38
        printf("%s\t%g\n", "float型の正の値の最小値", FLT_MIN);
			// FLT_MAX : 1.17549e-38 
        /* float型の最小値は-FLT_MAX */
        printf("%s\t%g\n", "double型の最大値", DBL_MAX);
			// DBL_MAX : 1.79769e+308 
        printf("%s\t%g\n", "double型の正の値の最小値", DBL_MIN);
			// DBL_MIN : 2.22507e-308 
        /* double型の最小値は-DBL_MAX */
        printf("%s\t%Lg\n", "long double型の最大値", LDBL_MAX);
			// LDBL_MAX : 1.18973e+4932 
        printf("%s\t%Lg\n", "long double型の正の値の最小値", LDBL_MIN);
			// LDBL_MIN : 3.3621e-4932 
        /* double型の最小値は-LDBL_MAX */


        return 0;
}

