#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>

#define CHILD_NUM 10
pid_t sig_pid[CHILD_NUM];
void sig_func(int signum)
{

	fprintf(stdout," child process.(%d)\n", signum);
/*
	while(1)
	{
		fprintf(stdout,"%d : child process.\tpid = %d.\tmy ppid = %d\n",iii,getpid(),getppid());
		sleep(5);
	}
*/
}

int main(void){
	pid_t result_pid;
	int i, iii;
	

	for(i = 0;i < CHILD_NUM;i++){
		iii = i ;
		result_pid = fork();
    
		switch(result_pid){
		case 0:
      /* getpidは自分のPIDを返す. */
      /* getppidは自分のPPID(親のPID)を返す */
//			while(1){
//				fprintf(stdout,"child process.\tpid = %d.\tmy ppid = %d\n",getpid(),getppid());
				fprintf(stdout,"child process.\tpid = %d.\tmy ppid = %d\n",getpid(),getppid());
				//sig_pid[i] = getpid() ;
				//signal( SIGUSR1, sig_func ) ;
				//sleep(1);
//			}
			break;
		case -1:
			fprintf(stderr,"fork failed.\n");
			break;
		default:
			sig_pid[i] = result_pid ;
			break;
		}
    /* 子は出る */
		if(result_pid == 0){
			return 0;
		}
	}

	//signal( SIGUSR1, sig_func ) ;
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
	return 0;
}



