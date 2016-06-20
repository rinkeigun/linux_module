/*
	2016/06/20 Huiqun.Lin
	mysql接続検証
	-------------------------------------------------
	次のエラーの時
	/tmp/ccyZlALg.o: 関数 `main' 内:
mysql_sample2.c:(.text+0x11): `mysql_init' に対する定義されていない参照です
mysql_sample2.c:(.text+0x59): `mysql_real_connect' に対する定義されていない参照です
mysql_sample2.c:(.text+0x69): `mysql_error' に対する定義されていない参照です
mysql_sample2.c:(.text+0x9b): `mysql_close' に対する定義されていない参照です
collect2: error: ld returned 1 exit status
	--------------------------------------------------
	mysql_config --libs
	gcc mysql_sample2.c -L/usr/lib/i386-linux-gnu -lmysqlclient
	--------------------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include <mysql/mysql.h>

#define DBHOST "localhost"
#define DBUSER "myuser"
#define DBPASS "mypass"
#define DBNAME "mydb"

int main()
{

       MYSQL *conn;
       MYSQL_RES *res;
       MYSQL_ROW row;

       // 接続
       conn = mysql_init(NULL);
       if (!mysql_real_connect(conn, DBHOST, DBUSER, DBPASS, DBNAME, 3306, NULL, 0)) {
          fprintf(stderr, "%s\n", mysql_error(conn));
          exit(1);
       }

       // 切断
       mysql_close(conn);

       return 0;
}

