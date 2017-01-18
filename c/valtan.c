/*
  valtan.c -- バルタン星人（もどき）が体操する(^^;)
*/
#include    <stdio.h>

#define  ESC    0x1B
#define  WAIT   (10000000 / 2)  /* 待ち時間 */
#define  LOOP   200             /* 繰り返し回数 */

void    main(void)
{
  int    xpos, ypos = 8;   /* x, y 座標 */
  int    i = 0;
  long   j;

  printf("%c[2J", ESC);    /* 画面消去 */
  printf("%c[>5h", ESC);   /* カーソル消去 */
  printf("%c[33m", ESC);   /* 文字を黄色に */

  for(i=0 ; i<LOOP; i+=2) {
    xpos = i % 80 + 1;
    if (xpos == 1)    ypos++;
    /* 腕を上げる */
    printf("%c[%d;%dH  Yo¥¥oY", ESC, ypos,   xpos);
    printf("%c[%d;%dH    w   ", ESC, ypos+1, xpos);
    printf("%c[%d;%dH   | |  ", ESC, ypos+2, xpos);
    for (j=0; j<WAIT; j++) { }
    /* 腕を下げる */
    printf("%c[%d;%dH   o¥¥o ", ESC, ypos,   xpos+1);
    printf("%c[%d;%dH >- w -<", ESC, ypos+1, xpos+1);
    printf("%c[%d;%dH   < >  ", ESC, ypos+2, xpos+1);
    for (j=0; j<WAIT; j++) { }
  }
  printf("¥nPress [Enter]");
  (void)getchar();        /* [Enter]キーを押せば終了 */
  printf("%c[>5l", ESC);  /* カーソル表示 */
  printf("%c[39m", ESC);  /* 文字色を戻す */
}