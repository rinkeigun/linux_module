#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

enum { MAXLINE = 1024 };
char *info = NULL;

void handler(int signum) {
  fprintf(stderr, info);
  free(info);
  info = NULL;
}

int main(void) {
  if (signal(SIGINT, handler) == SIG_ERR) {
    /* エラー処理 */
  }
  info = (char*)malloc(MAXLINE);
  if (info == NULL) {
    /* エラー処理 */
  }

  while (1) {
    fprintf(stderr, info);
  }
  free(info) ;
  return 0;
}
