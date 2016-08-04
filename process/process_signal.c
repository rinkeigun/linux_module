/*
	2016/08/03	Huiqun.Lin
	プロセス, シグナル生成例
*/
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

static int flg = 0 ;

void test_sig()
{
	printf("receive kill commands\n" ) ;
	flg ++ ;
}
int process()
{
  pid_t         p_id;
  int         status;
  int         return_code = 0;

  p_id = fork( ) ;
  if (p_id > 0) {
    	sleep(4);
      wait(&status);
      printf("親プロセス終了\n");
	}
  else if (p_id == 0) {
    /* 子プロセス */
    printf("子プロセス開始\n");
	signal(SIGUSR1, test_sig ) ;
	while(1)
	{

    	sleep(2);
		printf( "ここで無限ループ?\n" ) ;
		if( flg > 0 ) break ;
	}

    printf("子プロセス終了\n");
  }
  else {
    /* 親プロセス */
    if (p_id != -1) {
/*
      wait(&status);
    sleep(4);
      printf("親プロセス終了\n");
*/
    }
    else {
      perror("親プロセス : ");
      return_code = 1;
    }
  }

  return p_id;
}
int main()
{
	pid_t pid = process()  ;
	kill( SIGUSR1, pid ) ;
	printf( "process ID = %d\n", pid ) ;
}
