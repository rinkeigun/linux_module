# -*- coding: utf-8 -*-
# File name : fsqlite.py
# Date      : 2018/04/23
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import sqlite3
db = ':memory:'
tablename = 'wechat_control_t'
class run:
	def __init__(self):
		sql = "insert into %s values( '%s')" % (tablename, 1)
		self.exec(sql)
	def exec(self, sql):
		connector = sqlite3.connect(db)

		createtable = "create table IF NOT EXISTS %s (flg INTEGER)" % tablename
		connector.execute( createtable )
		connector.execute( sql )
		
		sql = "update %s set flg = %d " % ( tablename, 0 )
		connector.execute( sql )
		
		sql = "select flg from %s" % ( tablename )
		cur = connector.execute( sql )
		print( connector.execute( sql ).fetchone()[0] )



		connector.commit()
		connector.close()
# テストプログラムはこれより下に書く
if __name__ == '__main__':
	#sql = "insert into %s values( '%s', 'eCode', 'eType', 'python')" % (tablename, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	run()


