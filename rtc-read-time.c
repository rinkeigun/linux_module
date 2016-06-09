/*
        ~yas/syspro/time/rtc-read-time.c -- Read CMOS Realtime Clock in Linux
        Created on: 2011/01/28 17:12:36
*/


#include <sys/types.h>  /* open() */
#include <sys/stat.h>   /* open() */
#include <fcntl.h>      /* open() */
#include <sys/ioctl.h>  /* ioctl() */
#include <unistd.h>     /* close() */
#include <stdio.h>      /* printf() */
#include <stdlib.h>     /* exit() */
#include <linux/rtc.h>  /*  RTC_RD_TIME */

#define RTC_DEVICE_FILE "/dev/rtc"

main()
{
    int fd;
    struct rtc_time t1 ;
        if( (fd = open( RTC_DEVICE_FILE, O_RDONLY ))< 0 )
        {
            perror("open");
            exit( 1 );
        }
        if( ioctl( fd, RTC_RD_TIME, &t1 ) < 0 )
        {
            perror("ioctl(RTC_RD_TIME)");
            exit( 2 );
        }
        printf("%04d-%02d-%02d %02d:%02d:%02d\n",
                t1.tm_year+1900, t1.tm_mon+1, t1.tm_mday,
                t1.tm_hour, t1.tm_min, t1.tm_sec );
        close( fd );
}
