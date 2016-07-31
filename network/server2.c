/*
	2016/07/28 Huiqun.Lin
	mysql-config --libs
	gcc server2.c mysql_sample3.c -L/usr/lib/i386-linux-gnu -lmariadbclient
*/
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include "mysql_sample3.h"


int
main()
{
 int sock0;
 struct sockaddr_in addr;
 struct sockaddr_in client;
 int len;
 int sock;
int bin, lis, rcv, n ;

 sock0 = socket(AF_INET, SOCK_STREAM, 0);
 printf("sock0 = %d\n", sock0 ) ;

 addr.sin_family = AF_INET;
 addr.sin_port = htons(12345);
 addr.sin_addr.s_addr = INADDR_ANY;

 bin = bind(sock0, (struct sockaddr *)&addr, sizeof(addr));
if( bin == -1 )
{
	printf( "bind 失敗(errno : %d)\n", errno )  ;
}

 lis = listen(sock0, 1024);
	if( lis == -1 )
	{
		printf( "listen 失敗( errno : %d )\n", errno ) ;
	}


 while (1) {
	char msg[256] ;
	memset( msg, '\0', sizeof( msg ) ) ;
   len = sizeof(client);
   sock = accept(sock0, (struct sockaddr *)&client, &len);
	if( sock == -1 )
	{
		printf( "accept エラー( errno : %d ) \b", errno ) ;
	}
   //write(sock, "HELLO", 5);
   //read(sock, msg, 256 );
   //recv(sock, msg, 256, MSG_DONTWAIT );
printf("test %d\n" , n++) ;
   rcv = recv(sock, msg, 256, MSG_PEEK );
	if( rcv == -1 )
	{
		printf( "recv エラー( errno : %d )\n", errno ) ;
	}
	dbserver( msg ) ;	
	//printf( msg ) ;

   close(sock);
 }

 close(sock0);

 return 0;
}

