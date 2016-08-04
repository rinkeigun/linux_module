/*
	2016.08.04 Huiqun.Lin
	ps -ef | grep a.out
	defunct
*/
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>


int main(){
        int  pid = fork();

        if(pid == -1){
                printf("fork failed.\n");
        }else if(pid == 0){
                printf("child process. PID is %d\n",getpid());
        }else{
                sleep(10);
                printf("parent process. PID is %d\n",getpid());
        }

        return 0;
}
