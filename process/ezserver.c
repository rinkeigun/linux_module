#include "tcpserver.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>   /* memset() */
#include <unistd.h>   /* fork() */

#define SERVER_PORT     8080            /* サーバ用PORT */
#define SERVER_IP       0x00000000UL    /* サーバ用待ち受けIP */
#define BUFFER_SIZE     1024            /* バッファバイト数 */

/* prototypes */
int main(void );
int do_httpd(TCPCLIENT_INFO* client);

/* メイン */
int main(void)
{
    int ok = 1;             /* 1:処理続行 0:エラー発生 */
    TCPSERVER_INFO server;
    TCPCLIENT_INFO client;
    
    /* サーバの初期化 */
    if(ok) {
        /* server構造体初期化 */
        tcpserver_init(&server, SERVER_IP, SERVER_PORT);
        
        /* socket(), bind(), listen()をコール */
        ok = tcpserver_open(&server);
    }
    
    if(ok) {
        /* メインループ */
        while(tcpserver_wait(&server, &client)) {   /* クライアント接続待ち */
            /* クライアントから接続された */
       /* 子プロセス生成 */
       pid_t child_pid = fork();
       
       if(child_pid==-1) {
           /* fork()失敗→異常なのでサーバ終了 */
            break;
       }
       else if(child_pid==0) {
           /* 子プロセス */
           int ret = 0;
           /* 親プロセスのソケットを子プロセスに触らせたくないので
              クローズ */
           tcpserver_close(&server);
           
           /* 子プロセスはここで自ら終了 */
           exit(ret);
       }
       else {
            
            /* HTTPD処理 */
            do_httpd(&client);
            
            /* 後片付け：クライアントとの接続終了処理 */
            tcpclient_close(&client);    /* FIN,ACK送信 */
        }
    }
	}
    
    /* サーバの終了 */
    tcpserver_close(&server);
    return ok;
}

static const char *response_header =
    "HTTP/1.0 200 OK\r\n"
    "Server: ezhttpd(IPA Secure Programming Sample Program)\r\n"
    "Content-Type: text/html\r\n"
    "Content-Length: %d\r\n"
    "Connection: close\r\n"
    "\r\n";

static const char *response_body =
    "<HTML>\r\n"
    "<HEAD><TITLE>IPA Secure Programming - EZHTTPD</TITLE></HEAD>\r\n"
    "<BODY>\r\n"
    "<H1>IPA Secure Programming - EZHTTPD </H1>\r\n"
    "This page is from the EZHTTPD sample web server.\r\n"
    "</BODY>\r\n"
    "</HTML>\r\n";

/* クライアントとの処理(HTTP)をつかさどる */
/* 返り値 1:正常終了 0:異常終了 */
int do_httpd(TCPCLIENT_INFO* client)
{
    int     ok = 1;                 /* 正常終了時の返り値で初期化 */
    char    req_buf[BUFFER_SIZE];
    char    res_buf[BUFFER_SIZE];
    
    /* リクエストを読み込む */
    read(client->data_socket, req_buf, sizeof(req_buf));
    
    /* レスポンスを送信 */
    sprintf(res_buf, response_header, strlen(response_body));
    write(client->data_socket, res_buf, strlen(res_buf));
    write(client->data_socket, response_body, strlen(response_body));
    
    return ok;
}
