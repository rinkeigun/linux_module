/*
	2016/06/17 Huiqun.Lin
	タイマーの検証
	周期的な処理
	gcc -pthread timer.c
*/
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>
#include <signal.h>
#include <pthread.h>
#include <errno.h>

int main() {
        // setitimerにより通知されるシグナルをマスク
        sigset_t sigset;
        sigemptyset(&sigset);
        sigaddset(&sigset, SIGALRM);
        pthread_sigmask(SIG_BLOCK, &sigset, NULL);

        // タイマ設定　５秒毎に通知
        const struct timeval interval = { 5, 0 };
        const struct itimerval itimer = {interval, interval};
        int ret = setitimer(ITIMER_REAL, &itimer, NULL);
        if ( ret != 0 ) {
                perror("setitimer error");
                return -1;
        }

        int i;
        for ( i=0; i<10; i++ ) {
                int signo;
                sigwait(&sigset, &signo);

                struct timeval tv;
                gettimeofday(&tv, NULL);
                char    timebuf[26];
                ctime_r(&tv.tv_sec, timebuf);
                *strchr(timebuf, '\n') = '\0';
                printf("[%s] [%06d] signal[%d] recieved.\n",
                        timebuf, tv.tv_usec, signo);

                // たまに時間かかる処理がある想定
                if ( i % 4 == 3 ) {
                        unsigned int waittime = 7;
                        printf("wait %d seconds.\n", waittime);
                        sleep(waittime);
                }
        }

        return 0;
}
