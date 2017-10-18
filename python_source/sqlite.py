# -*- coding: utf-8-8 -*-

import sqlite3

connector = sqlite3.connect("sqlite_test.db")

sql = "create table IF NOT EXISTS test_table (id intager, name text)"
connector.execute( sql )
sql = "insert into test_table values('1', 'python')"
connector.execute( sql )
sql = "insert into test_table values('2', 'パイソン')"
connector.execute(sql)
sql = "insert into test_table values('3', 'ぱいそん')"
connector.execute( sql)

connector.commit()
connector.close()

