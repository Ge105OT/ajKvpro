# -*- coding: utf-8 -*-
#####################################
# author:起源者
# date:2017.7.20
# function:create sqlWorkSpace
####################################

import sqlite3

class Sqlite3Worker(object):

	"""docstring for Sqlite3Worker"""
	def __init__(self, FileName):
		super(Sqlite3Worker, self).__init__()
		self.sqlite3_conn = sqlite3.connect(FileName)
		self.sqlite3_cursor = self.sqlite3_conn.cursor()
		self.results = {}

	def execute(self, sql, values = None):
		values = values or []
		condition = sql.lower().strip()
		if condition.startswith("insert") or condition.startswith("INSERT") or \
			condition.startswith("create") or condition.startswith("CREATE") or \
			condition.startswith("update") or condition.startswith("UPDATE") or \
			condition.startswith("delete") or condition.startswith("DELETE"):
			self.insert_creat(sql, values)
		else:
			self.sql_execute(sql, values)
			return self.results		

	def insert_creat(self, sql, values):
		self.sqlite3_cursor.execute(sql, values)
		self.sqlite3_conn.commit()

	def sql_execute(self, sql , values = None):
		self.sqlite3_cursor.execute(sql, values)
		self.results = self.sqlite3_cursor.fetchall()

	def sqlClose(self):
		self.sqlite3_cursor.close()

# test
if __name__ == '__main__':
			sqlit = Sqlite3Worker('log.db')
			sqlit.execute("DROP TABLE IF EXISTS spiderurls")
			sqlit.execute('''CREATE TABLE IF NOT EXISTS spiderurls( 
					id INTEGER PRIMARY KEY, 
					url TEXT, 
					info TEXT
					)''')
			sqlit.execute('''CREATE TABLE IF NOT EXISTS user( 
					id INTEGER PRIMARY KEY, 
					url TEXT, 
					info TEXT
					)''')
			sqlit.execute("insert into spiderurls (id, url, info) values (1, 'http://192.168.126.1', 'gaywall');")
			results = sqlit.execute("SELECT * FROM spiderurls;")
			tableNames = sqlit.execute("select name from sqlite_master where type = 'table' order by name;")
			table_List = sqlit.execute("PRAGMA table_info(spiderurls);")
			sqlit.sqlClose()
			print results
			print table_List
			for i in tableNames:
				print i[0]