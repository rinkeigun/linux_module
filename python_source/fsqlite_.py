# -*- coding: utf-8 -*-
# File name : fsqlite.py
# Date      : 2017/11/12
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import sqlite3
import datetime
tablename = 'errorManagerT'
class run:
	def __init__(self):
		sql = "insert into %s values( '%s', 'eCode', 'eType', 'python')" % (tablename, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		self.exec(sql)
	def exec(self, sql):
		connector = sqlite3.connect("error.db")

		createtable = "create table IF NOT EXISTS %s (edt datetime, eCode text, eType text, eMessage text)" % tablename
		connector.execute( createtable )
		connector.execute( sql )

		connector.commit()
		connector.close()
# テストプログラムはこれより下に書く
if __name__ == '__main__':
	#sql = "insert into %s values( '%s', 'eCode', 'eType', 'python')" % (tablename, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	run()


