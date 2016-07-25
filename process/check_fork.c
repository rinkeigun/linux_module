#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
	FILE *f ;

int main(int argc, char** argv)
{
  pid_t pid;
  pid_t pid2[1];
  int status;
	
	int process_no = 1 ;
	int excu_times = 0 ;
	int excu_times_before = 0 ;
	int i ;
  
	printf( "top pid = %d\n", getpid() ) ;
	f = fopen( "test.txt", "a" ) ;
  /// 新しいプロセスを作る
  /// カーネルは、同じプロセスをもう１つ作る
	for( i=0; i<process_no; i++)
	{
  		pid = fork();
		printf("i=%d, pid=%d getpid=%d\n", i, pid, getpid() ) ;
if(0){

  		/// プロセス作成に失敗した時は、0未満を返す
 		 //if ( pid2[i] < 0 )
 		 if ( pid < 0 )
 		 {
   			 fprintf (stderr, "fork error\n");
   			 //exit(1);
  		}

  		/// 子プロセスのpidは、0
		pid2[i] = pid ;
 		if (pid2[i] == 0) 
  		//if (pid == 0) 
  		{
			char tmp_c[256] ;
			memset( tmp_c, '\0', sizeof( tmp_c )) ;
			sprintf( tmp_c, "aaaaa\t%d\t%d\n",i, getpid() ) ;
			//sprintf( tmp_c, "%d", pid2[i] ) ;
			printf( "%s\n", tmp_c ) ;
			if( 0>fwrite( tmp_c, sizeof ( tmp_c ), 1, f ) )
			{
	 
			    execl("/bin/echo", "echo", "hahaha", NULL);
			    perror("/bin/cat");
			}
//			sleep( 3 ) ;
    		//exit(-1);
  		}
	}
}

if(0)
{
	for( i=0; i<2; i++)
	{
		//  else
  		{
 		 	/// 子プロセスの終るのを待つ
   		 	//waitpid(pid2[i], &status, 0);
		//	pid = getpid() ;
		    pid = waitpid(-1, &status, 1);
		    //printf ("child(PID=%d) finished!\n", pid2[i]);
		    printf ("child(PID=%d) finished!\n", pid );

    
		    if (WIFEXITED(status)){
		   		/// 子プロセスがexit以外で終了した場合は0を返す
		   		/// exitで終了した時は、0以外を返す
		    	printf("exit, status=%d\n", WEXITSTATUS(status));
    		} else if (WIFSIGNALED(status)){
		      /// シグナルで終了していた時は0以外を返し、
		      /// それ以外は、0を返す
		      printf("signal, sig=%d\n", WTERMSIG(status));
    		} else {
     			 printf("abnormal exit\n");
    		}
		    //exit(0);
  		}

	}
}

  return(0);
}

