/*
	2016.07.27 Huiqun.Lin
	gcc -lwsock32 *.c -lws2_32
*/
	

#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include "serial.h"
#include "client.h"

int main (void)
{
	time_t timer;
	struct tm *local;
	serial_t obj = serial_create("COM6",9600);
	unsigned char buf[128], len;

	if ( obj == NULL ) {
		fprintf(stderr,"オブジェクト生成に失敗");
		return EXIT_FAILURE ;
	}

	while (1) {
		//memset( buf, '\0', sizeof(buf) ) ;
		memset( buf, '\0', strlen(buf) ) ;
		len = serial_recv(obj,buf,sizeof(buf));
    //if (len) serial_send(obj,buf,len);
		timer = time(NULL);
		local = localtime(&timer); /* 地方時に変換 */
//    if (len) printf("len=%d, %s",len, buf);
		if (len) {
			char msg[256];
			sprintf( msg, "%4d/%02d/%02d %02d:%02d:%02d temperature: %s",
				local->tm_year + 1900,
				local->tm_mon + 1,
				local->tm_mday,
				local->tm_hour,
				local->tm_min,
				local->tm_sec,
				buf);
			printf( msg ) ;
			client( msg ) ;
		}
		Sleep(5000);
		if ( kbhit() )  break;
	}

	serial_delete(obj);

	return EXIT_SUCCESS;
}

