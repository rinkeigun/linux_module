/*
	2016/09/12 Huiqun.Lin
	connect refused検証
*/

#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <errno.h>
#include <string.h>

int
main(int argc, char *argv[])
{
 struct sockaddr_in server;
 struct sockaddr_in client_addr;
 int sock;
 char buf[32];
 char *deststr;
 unsigned int **addrptr;

	struct timeval  timeout;
	fd_set          readfds;
	int yes = 1 ;

 if (argc != 2) {
	 printf("Usage : %s dest\n", argv[0]);
	 return 1;
 }
 deststr = argv[1];

 sock = socket(AF_INET, SOCK_STREAM, 0);
	if( sock == -1 )
	{
		printf( "%d:%s\n", errno, strerror( errno ) ) ;
		return 1 ;
	}

//    setsockopt(sock,
//       SOL_SOCKET, SO_REUSEADDR, (const char *)&yes, sizeof(yes));
	memset( &client_addr, 0, sizeof( client_addr ) ) ;
	memset( &server, 0, sizeof( server ) ) ;
 client_addr.sin_family = AF_INET;
 client_addr.sin_port = htons(10000);
 client_addr.sin_addr.s_addr = inet_addr("172.30.10.15");

    if(bind(sock,(struct sockaddr *)&client_addr,sizeof(client_addr)) == -1)
    {
        printf("クライアントのバインドに失敗しました errno(%d):%s", errno, strerror( errno ) );
    }
printf( "port %d\n", client_addr.sin_port ) ;

 server.sin_family = PF_INET;
 server.sin_port = htons(10000);
 server.sin_addr.s_addr = inet_addr(deststr);

    FD_ZERO(&readfds);
    FD_SET(sock,&readfds);
    timeout.tv_sec=0;
    timeout.tv_usec=0;
 if (server.sin_addr.s_addr == 0xffffffff) {
	 struct hostent *host;

	 host = gethostbyname(deststr);
	 if (host == NULL) {
		 return 1;
	 }

	 addrptr = (unsigned int **)host->h_addr_list;

	 while (*addrptr != NULL) {
		 server.sin_addr.s_addr = *(*addrptr);

		 /* connect()が成功したらloopを抜けます */
		 if (connect(sock,
				(struct sockaddr *)&server,
				sizeof(server)) == 0) {
			break;
		 }

		 addrptr++;
	 }
 } else {
	 /* inet_addr()が成功したとき */
	 if (connect(sock,
                     (struct sockaddr *)&server,
                     sizeof(server)) != 0) {
		 perror("connect");
		 return 1;
	 }
 }

 /* 本当はconnect()が成功したかどうかを判断してから次に進むべきです */

 memset(buf, 0, sizeof(buf));
 int n = recv(sock, buf, sizeof(buf), 0);

 printf("%d, %s\n", n, buf);

 close(sock);

 return 0;
}

