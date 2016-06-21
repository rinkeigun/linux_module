#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>

int
main()
{
 int sock;

 //sock = socket(AF_INET /* IPv4 */, SOCK_STREAM /* TCP */, 0);
 sock = socket(3000 /* IPv4 */, 4000 /* TCP */, 5000);
 if (sock < 0) {
	perror( "socket" ) ;
	printf("errno : %d\n", errno );
	return 1;
 }

 return 0;
}


