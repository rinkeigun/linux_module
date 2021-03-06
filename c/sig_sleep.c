#include <stdio.h>
#include <assert.h>
#include <signal.h>
#include <unistd.h>

static volatile int count = 0;

static void handler(int sig)
{
    assert(sig == SIGINT);
    count++;
}

int main()
{
	int left_i = 0 ;

#if 0
	// シグナル登録してある時に登録のhandlerで実行、登録してない時デフォールト動作
    if (signal(SIGINT, handler) == SIG_ERR)
        return 1;
#endif

    while (count < 3) {
        left_i = sleep(10); //sigを受けた後残る時間を返す
		printf( "left_i = %d\n", left_i ) ;
    }
    return 0;
}

