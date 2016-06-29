/*
	2016/06/28	Huiqun.Lin
 */
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
 
#include <sys/types.h>	// fork
#include <unistd.h>	// fork
#include <sys/wait.h>	// wait
 
#include <err.h>
#include <errno.h>
 
pid_t
Waitpid(pid_t wpid, int *status, int options)
{
	for(;;){
		pid_t pid = waitpid(wpid, status, options);
		if (-1 == pid){
			if (EINTR == errno){
				(void) printf ("EINTR\n");
				continue;
			}
			if (ECHILD == errno){
				(void) printf("no child\n");
			}
			else {
				err(EXIT_FAILURE, "can not wait");
			}
		}
		return (pid);
	}
}
 
void
wait_children (ssize_t *child) {
	int status;
	//int options = WEXITED;
	int options = 1;
 
	bool is_first = true;
	for(;*child > 0;) {
		pid_t pid = Waitpid(-1, &status, options);
		if (-1 == pid) {
			return;
		} else if (0 == pid) {
			return;
		}
		(*child)--;
		if (is_first) {
			is_first = false;
			options = WNOHANG;
		}
	}
}
 
void
doit(int cnt)
{
	srandom( getpid() );
	unsigned int sleep_sec = random() % cnt;
	sleep (sleep_sec);
	printf("cnt = %d, sec = %d\n", cnt, sleep_sec ) ;
}
 
int
main(int argc, char *argv[])
{
	const ssize_t child_max = 30;	// 同時最大子プロセス数
	ssize_t child = 0;				// 現在の子プロセスの数
 
	ssize_t i = 0;
	while(1){
		//(void) printf ("child=%lu\n",  child);
		printf ("child=%lu\n",  child);
		for (; child < child_max; child++/*, fork_count++*/) {
			pid_t pid = fork();
			if (-1 == pid) {
				err(EXIT_FAILURE, "can not fork");
			}
			else if (0 == pid) {
				doit(2);
				printf(" parent\n" ) ;
				_exit(EXIT_SUCCESS);
			}
			else if( 0< pid ){
				doit(2);
				printf(" child\n" ) ;
			}
		}
		wait_children(&child);
	}
	while (child > 0) {
		wait_children(&child);
	}
 
	exit (EXIT_SUCCESS);
}
