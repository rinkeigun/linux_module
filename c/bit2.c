#include <stdio.h>

/* 符号無し char 型の値と，そのビットの状態を表示する */
void show_signed_char(signed char x)
{
  int i;

  printf("%4d  %02x  ", x, (unsigned char)x);
  for (i = 7; i >= 0; i--) {
    printf("%d", (x>>i) & 1);
  }
  printf("\n");
}


int main()
{
  show_signed_char(-130);
  show_signed_char(-129);
  show_signed_char(-128);
  show_signed_char(-127);
  show_signed_char(-3);
  show_signed_char(-2);
  show_signed_char(-1);
  show_signed_char(0);
  show_signed_char(1);
  show_signed_char(2);
  show_signed_char(3);
  show_signed_char(126);
  show_signed_char(127);
  show_signed_char(128);
  show_signed_char(129);

  return 0;
}

