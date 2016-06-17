/*
	2016/06/17 Huiqun.Lin
	stack検証

------------------------------------------------
	address = 0xbfc4c53c
	address = 0xbfc4c50c
	...............
	address = 0xbf56268c
	address = 0xbf56265c
	Segmentation fault
------------------------------------------------
*/

#include <stdio.h>

void func(void)
{
    int a = 4 ;
    printf("address = %p\n",&a);
    func();
}

int main(void)
{
    func();

    return(0);
}


