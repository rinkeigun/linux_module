/*
	2016/06/20	Huiqun.Lin
	MySQLにデータを取得する。DB環境がないので例はテストしない
	gcc mysql_sample3.c -L/usr/lib/i386-linux-gnu -lmysqlclient
*/

#include "mysql_sample3.h"

int dbserver(char *str)
{

       MYSQL *conn;
       MYSQL_RES *res;
       MYSQL_ROW row;
		char sql[256] ;

       // 接続
		memset( sql, '\0', 256 ) ;
       conn = mysql_init(NULL);
       if (!mysql_real_connect(conn, DBHOST, DBUSER, DBPASS, DBNAME, 3306, NULL, 0)) {
          fprintf(stderr, "%s\n", mysql_error(conn));
          exit(1);
       }

       // クエリ発行
            //if (mysql_query(conn, "show tables")) {
            sprintf( sql, "insert into feature ( b ) values ( '%s' ) ;", str ) ; 
            if (mysql_query(conn, sql)) {
                fprintf(stderr, "%s\n", mysql_error(conn));
                exit(1);
            }
            res = mysql_use_result(conn);

       // 結果表示
        //while ((row = mysql_fetch_row(res)) != NULL) {
        //    printf("%s\n", row[0]);
       // }
       mysql_free_result(res);

       // 切断
       mysql_close(conn);

       return 0;
}

