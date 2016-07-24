#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <stdlib.h>
#include "serial.h"
int main (void)
{
  serial_t obj = serial_create("COM6",9600);
  unsigned char buf[128], len;

  if ( obj == NULL ) {
    fprintf(stderr,"オブジェクト生成に失敗");
    return EXIT_FAILURE;
  }

  while (1) {
	memset( buf, '\0', sizeof(buf) ) ;
    len = serial_recv(obj,buf,sizeof(buf));
    //if (len) serial_send(obj,buf,len);
    if (len) printf("len=%d, %s",len, buf);
    Sleep(1000);
    if ( kbhit() )  break;
  }

  serial_delete(obj);

  return EXIT_SUCCESS;
}

