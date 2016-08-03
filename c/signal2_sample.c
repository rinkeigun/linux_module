/*
	2016.08.03 Huiqun.Lin
	kill -USR1 16351 ← ./a.out の PID
*/
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
 
static int g_hoge = 0;
 
/* シグナルハンドラ */
void sig_handler(int signo)
{
    if (signo == SIGUSR1) {
        printf("received SIGUSR1\n");
    } else if (signo == SIGKILL) {
        printf("received SIGKILL\n");
    } else if (signo == SIGSTOP) {
        printf("received SIGSTOP\n");
    } else if (signo == SIGTERM) {
        printf("received SIGTERM\n");
    }
    g_hoge = 1;
}
 
int main(void)
{
    /* シグナルハンドラの設定 */
    if (signal(SIGUSR1, sig_handler) == SIG_ERR) {
        printf("\ncan't catch SIGUSR1\n");
    }
 
    /* シグナルハンドラの設定 */
    if (signal(SIGTERM, sig_handler) == SIG_ERR) {
        printf("\ncan't catch SIGUSR1\n");
    }
 
    /* シグナルハンドラの設定 */
    if (signal(SIGKILL, sig_handler) == SIG_ERR) {
        printf("\ncan't catch SIGKILL\n");
    }
 
    /* シグナルハンドラの設定 */
    if (signal(SIGSTOP, sig_handler) == SIG_ERR) {
        printf("\ncan't catch SIGSTOP\n");
    }
 
    /* シグナルを受け取るまで無限ループ */
    while(1) {
        if (g_hoge == 1) break;
        sleep(1);
    }
 
    printf("the end\n");
    return 0;
}

