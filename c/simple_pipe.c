#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    pid_t pid ;
    char buffer[256];
    int pp[2];

    /*  パイプの作成 */
    pipe(pp);

    pid = fork();  /* 子のプロセスの生成 */

    /*  子プロセスの動き */
    if ( pid == 0 )
       {
       close(pp[0]);
       fgets(buffer,256,stdin);
       write(pp[1],buffer,strlen(buffer)+1); /* パイプへ書き込み */
       close(pp[1]);
       }
    /*  親プロセスの動き */
    else
       {
       close(pp[1]);
       read(pp[0],buffer,256); /* パイプから読み込み */
       printf("Message From Child : %s\n",buffer);
       close(pp[0]);
       }

return(0);
}
