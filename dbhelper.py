import mysql.connector

class DBhelper:

	def __init__(self):
		try:
			self.conn = mysql.connector.connect(
				host = "localhost",
				username = "root",
				password = "",
				database = "py_mysql" 
				)

			self.mycursor = self.conn.cursor()
		except:
			print("connected to Database")
		else:
			print("Error, could't connect to Database ")

	def register(self, name, email, password):
		try:
			self.mycursor.execute("""
				INSERT INTO 'user' ('id, 'name', 'email', 'password') VALUES (NULL, '{}','{}','{}',);
				""".format(name, email, password))
			self.conn.commit()
		except:
			return -1
		else:
			return 1
