#include <stdio.h>
#include <limits.h>
#include <float.h>

int main (int argc, char **argv)
{
        printf("%s\t%d\n", "char型の最大値", CHAR_MAX);
        printf("%s\t%d\n", "char型の最小値", CHAR_MIN);
        printf("%s\t%d\n", "signed char型の最大値", SCHAR_MAX);
        printf("%s\t%d\n", "signed char型の最小値", SCHAR_MIN);
        printf("%s\t%d\n", "unsigned char型の最大値", UCHAR_MAX);
        printf("%s\t%d\n", "short型の最大値", SHRT_MAX);
        printf("%s\t%d\n", "short型の最小値", SHRT_MIN);
        printf("%s\t%d\n", "unsigned short型の最大値", USHRT_MAX);
        printf("%s\t%d\n", "int型の最大値", INT_MAX);
        printf("%s\t%d\n", "int型の最小値", INT_MIN);
        printf("%s\t%u\n", "unsigned int型の最大値", UINT_MAX);
        printf("%s\t%ld\n", "long型の最大値", LONG_MAX);
        printf("%s\t%ld\n", "long型の最小値", LONG_MIN);
        printf("%s\t%lu\n", "unsigned long型の最大値", ULONG_MAX);
        printf("%s\t%g\n", "float型の最大値", FLT_MAX);
        printf("%s\t%g\n", "float型の正の値の最小値", FLT_MIN);
        /* float型の最小値は-FLT_MAX */
        printf("%s\t%g\n", "double型の最大値", DBL_MAX);
        printf("%s\t%g\n", "double型の正の値の最小値", DBL_MIN);
        /* double型の最小値は-DBL_MAX */
        printf("%s\t%Lg\n", "long double型の最大値", LDBL_MAX);
        printf("%s\t%Lg\n", "long double型の正の値の最小値", LDBL_MIN);
        /* double型の最小値は-LDBL_MAX */

        return 0;
}

