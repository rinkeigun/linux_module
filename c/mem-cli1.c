#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct transfer_data {
    int  no ;
    char name[10];
    int  flag ; /*  0:未入力 1:入力済み 2:サーバーで出力済み */
};  /* 共有メモリに渡すデータの構造 */

int main(void)
{
    char no[10] ; 
    int shmid ;
    void *shared_mem ;

    /* 共有メモリのアドレスを格納する変数の宣言 */
    struct transfer_data *mem ;

    shmid = shmget( (key_t)12345 , 100 , 0777 | IPC_CREAT );
    shared_mem = shmat(shmid,(void *)0 ,0 );

    /* 取得した共有メモリのアドレスを変数 mem へ代入 */
    mem = (struct transfer_data *)shared_mem ;

    mem->flag = 0 ;

    printf("No = ");
    fgets(no,10,stdin);
    mem->no = atoi(no);

    printf("name = ");
    fgets(mem->name,10,stdin);

    mem->flag = 1 ;
    while(1)
        {
        if ( mem->flag == 2 ) break ;
        }

    shmdt(shared_mem);

    return(0);
}


