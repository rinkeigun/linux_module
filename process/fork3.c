/*
	2016/08/04	Huiqun.Lin
	複数の子プロセスの生成
*/
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

#define CHILD_NUM 2
pid_t sig_pid[CHILD_NUM];
int main(void){
	pid_t result_pid;
	int i, cnt=0;
	

	for(i = 0;i < CHILD_NUM;i++){
		printf( "forkは一回実行することにより\n" ) ;
		result_pid = fork();
		printf( "forkの後ろのコードは必ず２回実行される。親と子はどっち先に生成されるか？\n" ) ;
    
		switch(result_pid){
		case 0:
      /* getpidは自分のPIDを返す. */
      /* getppidは自分のPPID(親のPID)を返す */
				fprintf(stdout,"child : child process.\tpid = %d.\tmy ppid = %d\n",getpid(),getppid());
/*
				signal( SIGUSR1, sig_func ) ;
				while(1){
					fprintf(stdout,"1  child process.\tpid = %d.\tmy ppid = %d\n",getpid(),getppid());
					sleep(1) ;
				}
*/
				//sig_pid[i] = getpid() ;
				//sleep(1);
//			}
			break;
		case -1:
			fprintf(stderr,"fork failed.\n");
			break;
		default:
			sig_pid[i] = result_pid ;
			fprintf(stdout,"parent : child process.\tpid = %d.\tmy ppid = %d\n",result_pid, getpid());
			break;
		}
    	/* 子は出る */
		if(result_pid == 0){
			printf( "子プロセスの時にreturnしないと余分なプロセスが生成される\n" ) ;
			return 0;
		}
	}

	//signal( SIGUSR1, sig_func ) ;
#if 0
	sleep(5) ;

	for( i=0; i<CHILD_NUM; i++)
	{
		printf("regist pid[%d] = %d\n", i, sig_pid[i] ) ;
		kill(sig_pid[i], SIGUSR1 ) ; 
		sleep( 2 ) ;
	}

	/* 親だけ実行 */
	if(result_pid != 0){
		int status;
		int child_pid;
		i = 0;
		printf("parent process\n");
		while(i < CHILD_NUM){
			child_pid = waitpid(-1,&status,WNOHANG);
			if(child_pid > 0){
				i++;
				fprintf(stdout,"PID %d done\n",child_pid);
			}else{
				fprintf(stdout,"No child exited\n");
			}
			sleep(1);
		}
	}
#endif
	return 0;
}


