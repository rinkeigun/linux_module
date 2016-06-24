/*
 * tcpserver.c  --- Copyright (c) 2001 Masaru Matsunami
 *                  All rights reserved.
 */

#include "tcpserver.h"
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <strings.h>
#include <errno.h>

/* TCPSERVER_INFO構造体の初期化 */
void tcpserver_init(
    TCPSERVER_INFO* server_info,
    unsigned long   ip,
    unsigned short  port)
{
    /* まずはゼロクリア */
    memset(server_info, 0, sizeof(*server_info));
    
    /* socket()がエラーのとき-1を返すことを考慮し-1と初期化 */
    /* エラー後にtcpserver_close()でソケットクローズしないための工夫 */
    server_info->wait_socket = -1;
    
    /* IPアドレスとポート番号をセット */
    server_info->server_addr.sin_family     = AF_INET;      /* TCP/IP */
    server_info->server_addr.sin_addr.s_addr= htonl(ip);    /* IPアドレス */
    server_info->server_addr.sin_port       = htons(port);  /* ポート番号 */
}

/* サーバ待ち受け用ソケットの作成・設置 */
/* 帰り値 1:成功 0:エラー */
int tcpserver_open(TCPSERVER_INFO* server_info)
{
    /* TCPソケットを作成 */
    server_info->wait_socket = socket(PF_INET, SOCK_STREAM, 0);
    if(server_info->wait_socket==-1) {
        /* ソケット作成の失敗 */
        perror("tcpserver_open.socket");
        return 0;
    }
    
    /* TCPソケットを設置 */
    /* これによりサーバ側のポート（クライアント待ち受け用）を占有する */
    /* このときTCPソケットの状態はクローズ（CLOSE）となる */
    if(bind(server_info->wait_socket,
            (struct sockaddr*)&server_info->server_addr,
            sizeof(server_info->server_addr))==-1)
    {
        /* ソケット設置の失敗 - 主に以下の2つが原因 */
        /* (1)ポートが既に使用されている */
        /* (2)ポート番号が1023以下であるにも関わらず一般ユーザ権限で実行 */
        perror("tcpserver_open.bind");
        return 0;
    }
    
    /* TCPソケットをクライアント接続待ち状態（LISTEN）にする */
    if(listen(server_info->wait_socket, 5)==-1) {
        /* 普通はこんなところでは失敗しない→異常？ */
        perror("tcpserver_open.listen");
        return 0;
    }
    
    /* 正常終了 */
    return 1;
}

/* サーバ待ち受け用ソケットの開放 */
void tcpserver_close(TCPSERVER_INFO* server_info)
{
    /* ソケットがオープンされているならクローズする */
    if(server_info->wait_socket != -1) {
        close(server_info->wait_socket);
        server_info->wait_socket = -1;
    }
}

/* クライアントからの接続を待機・確立 */
/* 帰り値 1:クライアントとの接続を確立した 0:エラー */
int tcpserver_wait(
    TCPSERVER_INFO* server_info,    /* tcpserver_init()で初期化したもの */
    TCPCLIENT_INFO* client_info)    /* 接続してきたクライアントの情報が入る */
{
    /* client_info構造体を初期化 */
    memset(client_info, 0, sizeof(*client_info));   /* ゼロクリア */
    client_info->data_socket = -1;      /* accept()のエラー値で初期化 */
    
    /* クライアント接続を待機し，接続されたらデータ送受用ソケットを取得 */
    /* for(;;)ループはシグナル受信時に再accept()するため必要 */
    for(;;) {
        socklen_t client_addr_len = sizeof(client_info->client_addr);
        client_info->data_socket =
            accept(server_info->wait_socket,
                    (struct sockaddr*)&client_info->client_addr,
                    &client_addr_len);
        
        /* accept()の返り値チェック */
        if(client_info->data_socket!=-1) break; /* 正常終了 */
        if(errno==EINTR) continue;              /* シグナル受信→再accept() */
        perror("tcpserver_open.accept");        /* やっぱりエラー */
        return 0;   /* エラー終了 */
    }
    
    /* 正常終了 */
    return 1;
}

/* クライアントとの接続を切断 */
void tcpclient_close(
    TCPCLIENT_INFO* client_info)    /* 接続してきたクライアントの情報が入る */
{
    /* ソケットがオープンされているならクローズする */
    if(client_info->data_socket != -1) {
        close(client_info->data_socket);                /* ソケットクローズ */
        client_info->data_socket = -1;
    }
}
