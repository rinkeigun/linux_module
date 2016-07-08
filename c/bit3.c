#include <stdio.h>

#define bitcheck(a,b) ((a) >> (b)) & 1
#define bitset(a,b)     (a) |= (1 << (b))
#define bitunset(a,b)  (a) &= ~(1 << (b))

int main(void)
{
    int i, check, maxbit;

    maxbit = sizeof(int) * 8 - 1;
    check  = 1234567890;

    for (i = maxbit; i >= 0; i--) {
        printf("%d", bitcheck(check, i));
    }
    printf("\n");


    bitset(check, 3);
    bitset(check, 10);

    for (i = maxbit; i >= 0; i--) {
        printf("%d", bitcheck(check, i));
    }
    printf("\n");


    bitunset(check, 1);
    bitunset(check, 4);

    for (i = maxbit; i >= 0; i--) {
        printf("%d", bitcheck(check, i));
    }
    printf("\n");

    return 0;
}

