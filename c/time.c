#include <stdio.h>
#include <time.h>

int main(void)
{
  clock_t start, end;
  int i;

  start = clock();
  printf( "開始時間:%d\n", start );

  /* 何かの処理 */
  for( i=0; i<500000000; i++ );

  end = clock();
  printf( "終了時間:%d\n", end );
  printf( "処理時間:%d[ms]\n", end - start );

  return 0;
}
