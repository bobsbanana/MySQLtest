import mysql.connector
class _Datatools:
	def __init__(self,db):
		self.db = db
		self.cursor = db.cursor(buffered=True)
	def setDB(self,db):
		self.db = db
	def getDB(self):
		return self.db
	def setCursor(self,db):
		self.cursor = db.cursor
	def getCursor(self):
		return db.cursor
	def showTables(self):
		self.cursor.execute("SHOW TABLES")
		for x in self.cursor:
			print(x)
	def showUserStats(self, username):
		val = (username,)
		sql = "SELECT username,passwd FROM userInfo WHERE username=%s"
		self.cursor.execute(sql,val)
		for i in self.cursor:
			print(i)
	def deleteUser(self,username):
		val = (username,)
		sql = "DELETE FROM userInfo WHERE username=%s"
		self.cursor.execute(sql,val)
		self.db.commit()
		print(self.cursor.rowcount, "record(s) deleted")
	def addUser(self, tablename, username, passwd):
		val = (username,passwd,)
		sql = "INSERT INTO {} (username, passwd) VALUES (%s, %s)".format(tablename)
		self.cursor.execute(sql,val)
		self.db.commit()
		print(self.cursor.rowcount, "record(s) added")
	def displayDatabase(self):
		sql = "SELECT * FROM userInfo"
		self.cursor.execute(sql)
		gap = " "*3
		print("="*33)
		heading = f"{'ID':3s}{gap}{'USERNAME':15}{gap}{'PASSWORD':15}"
		print(heading)
		print("-"*33)
		for x in self.cursor:
			ide = str(x[2])
			line = f"{ide:3s}{gap}{x[0]:15}{gap}{x[1]:15}"
			print(line)
		print("="*33)