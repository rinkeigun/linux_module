/*
	2016/06/20	Huiqun.Lin
	MySQLにデータを取得する。DB環境がないので例はテストしない
	gcc mysql_sample3.c -L/usr/lib/i386-linux-gnu -lmysqlclient
*/

#ifndef _DBSERVER_H_
#define _DBSERVER_H_
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql/mysql.h>

#define DBHOST "localhost"
#define DBUSER "root"
#define DBPASS "Keigun690920"
#define DBNAME "hardware_info"

int dbserver(char *str) ;

#endif
