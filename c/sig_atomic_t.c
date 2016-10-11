#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <stdarg.h>

enum { MAXLINE = 1024 };
volatile sig_atomic_t eflag = 0;
char *info = NULL;

void handler(int signum) {
  eflag = 1;
}

int main(void) {
  if (signal(SIGINT, handler) == SIG_ERR) {
    /* エラー処理 */
  }
  info = (char*)malloc(MAXLINE);
  if (info == NULL) {
    /* エラー処理 */
  }

  while (!eflag) {
    fprintf(stderr, info);	
  }

  fprintf(stderr, info);
  free(info);
  info = NULL;

  return 0;
}
