/*
 * tcpserver.h  --- Copyright (c) 2001 Masaru Matsunami
 *                  All rights reserved.
 */
 
/*
 * 使い方
 *
 *  TCPSERVER_INFO server;
 *  tcpserver_init(&server, 0, 1234);           ポート1234でサービス提供
 *  tcpserver_open(&server);                    ポート1234をbind(), listen()
 *  for(;;) {
 *      TCPCLIENT_INFO client;
 *      tcpserver_wait(&server, &client);       クライアント接続を待つ
 *      spawn_child_process(&server, &client);  子プロセスを生成し
 *  }                                           クライアントと通信させる
 *  
 *  spawn_child_process()関数で，fork()などして，
 *  client->data_socketに対してread()，write()することで，
 *  クライアントと通信する
 *
 *  サンプルはこちら
 *
 *  void spawn_child_process(TCPSERVER_INFO *server, TCPCLIENT_INFO *client) {
 *      int child_pid = fork();
 *      switch(child_pic) {
 *      case -1:    ← fork()でエラー発生
 *          return;
 *      case 0:     ← 子プロセスの処理
 *          close_parent_fds();
 *          exit(do_service_for_client(client));
 *          break;
 *      default:    ← 親プロセスは何もせず
 *          tcpclient_close(client);
 *          return; ← そのままリターン
 *      }
 *  }
 */

#ifndef _TCPSERVER_H_
#define _TCPSERVER_H_

#include "std_header.h"
#include <sys/socket.h>
#include <netinet/in.h>

/* クライアントからの接続を待つサーバの情報を表現する構造体 */
typedef struct {
    int                 wait_socket;    /* サーバ待ち受け用ソケット */
    struct sockaddr_in  server_addr;    /* サーバ待ち受け用アドレス */
} TCPSERVER_INFO;

/* クライアントとの接続に関する情報を保存する構造体 */
typedef struct {
    int                 data_socket;    /* クライアントとの通信用ソケット */
    struct sockaddr_in  client_addr;    /* クライアントのアドレス */
} TCPCLIENT_INFO;

/* TCPSERVER_INFO構造体の初期化 */
extern void tcpserver_init(
    TCPSERVER_INFO* server_info,    /* ←この構造体を初期化する */
    unsigned long   ip,             /* サーバ待受IPアドレス（32ビット値） */
    unsigned short  port);          /* サーバ待受ポート番号 */

/* サーバ側ソケットの作成・設置 */
extern int tcpserver_open(          /* 帰り値 1:成功 0:エラー */
    TCPSERVER_INFO* server_info);

/* サーバ側ソケットの開放 */
extern void tcpserver_close(
    TCPSERVER_INFO* server_info);

/* クライアントからの接続を待機・確立 */
/* 帰り値 1:クライアントとの接続を確立した 0:エラー */
extern int tcpserver_wait(
    TCPSERVER_INFO* server_info,    /* tcpserver_init()で初期化したもの */
    TCPCLIENT_INFO* client_info);   /* 接続してきたクライアントの情報が入る */

/* クライアントとの接続を終了 */
extern void tcpclient_close(
    TCPCLIENT_INFO* client_info);   /* tcpserver_wait()で初期化されたもの */

extern int tcp_main( void );   /* */

#endif

