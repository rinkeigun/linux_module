#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define COUNTRY_NUM (8)

/* 列挙型の宣言 */
enum country { USA, UK, ITALY, CANADA, 
               GERMANY, JAPAN, FRANCE, RUSSIA };

int main (int argc, char **argv)
{
        enum country c;

        /* ランダムに国を選ぶ */
        srand(time(NULL));
        c = rand()%COUNTRY_NUM;

        /* 正式名称を表示 */
        switch(c) {
        case USA:
                printf("United States of America\n");
                break;
        case UK:
                printf("United Kingdom of Great Britain and Northern Ireland\n");
                break;
        case ITALY:
                printf("Italian Republic\n");
                break;
        case CANADA:
                printf("Canada\n");
                break;
        case GERMANY:
                printf("Federal Republic of Germany\n");
                break;
        case JAPAN:
                printf("Japan\n");
                break;
        case FRANCE:
                printf("French Republic\n");
                break;
        case RUSSIA:
                printf("Russian Federation\n");
                break;
        }

        return 0;
}
