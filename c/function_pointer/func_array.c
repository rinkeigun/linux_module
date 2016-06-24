/*
        proverb.c
        指定の数に関係することわざ・慣用句を表示する
*/
/* インクルード */
#include <stdio.h>

/* プロトタイプ宣言 */
void proverb0(void);
void proverb1(void);
void proverb2(void);
void proverb3(void);
void proverb4(void);
void proverb5(void);
void proverb6(void);
void proverb7(void);
void proverb8(void);
void proverb9(void);
void proverbOthers(void);

/* typedef */
typedef void (*PROVERB_FUNC)(void);

int main(int argc, char *argv[])
{
        int n = 0;
        PROVERB_FUNC f[] = {
                proverb0, proverb1, proverb2, proverb3, proverb4, proverb5, 
                proverb6, proverb7, proverb8, proverb9, proverbOthers
        };

        /* 引数のチェック */
        if (argc != 2) {
                printf("Usage: %s <number> \n", argv[0]);
                return 0;
        }

        /* 引数をintに変換 */
        n = atoi(argv[1]);
        if ((n < 0) || (n > 9)) {
                n = 10;
        }

        /* 引数に対応する関数テーブル上の関数をコール */
        (*f[n])();

        return 0;
}


void proverb0(void)
{
        printf("%s\n", "【零の数がつくことわざ・慣用句】");
        printf("%s\n", "零零細細");
}

void proverb1(void)
{
        printf("%s\n", "1");
}

void proverb2(void)
{
        printf("%s\n", "2.【零の数がつくことわざ・慣用句】");
}

void proverb3(void)
{
        printf("%s\n", "3.【零の数がつくことわざ・慣用句】");
}

void proverb4(void)
{
        printf("%s\n", "4.【零の数がつくことわざ・慣用句】");
}

void proverb5(void)
{
        printf("%s\n", "5.【零の数がつくことわざ・慣用句】");
}

void proverb6(void)
{
        printf("%s\n", "6.【零の数がつくことわざ・慣用句】");
}

void proverb7(void)
{
        printf("%s\n", "7.【零の数がつくことわざ・慣用句】");
}

void proverb8(void)
{
        printf("%s\n", "8.【零の数がつくことわざ・慣用句】");
}

void proverb9(void)
{
        printf("%s\n", "9.【零の数がつくことわざ・慣用句】");
}

void proverbOthers(void)
{
        printf("%s\n", "others.【零の数がつくことわざ・慣用句】");
}



