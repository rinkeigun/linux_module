#ifndef _CLIENT_H_
#define _CLIENT_H_

#include <stdio.h>
#include <string.h>
#include <sys/types.h>

#include <winsock2.h>
#include <ws2tcpip.h>
#include <errno.h>
/*
#include <sys/socket.h>
#include <netinet/in.h>
*/
/* 関数プロトタイプ */
int client( char *);

#endif /* _CLIENT_H_ */

