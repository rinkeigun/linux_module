/*
	2016/06/20	Huiqun.Lin
	プロセス生成例
*/
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
  int         p_id;
  int         status;
  int         return_code = 0;

  if ((p_id = fork()) == 0) {
    /* 子プロセス */
    printf("子プロセス開始\n");

    sleep(2);

    printf("子プロセス終了\n");
  }
  else {
    /* 親プロセス */
    if (p_id != -1) {
      wait(&status);
      printf("親プロセス終了\n");
    }
    else {
      perror("親プロセス : ");
      return_code = 1;
    }
  }

  return return_code;
}
