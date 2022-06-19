import sys
from dbhelper import DBhelper

class Flipkart:

	def __init__(self):
		# connect to the database
		self.db = DBhelper()
		self.menu()

	def menu(self):

		user_input = input("""
			1. Register
			2. Login
			3. Exit
			""")

		if user_input == "1":
			self.register()
		elif user_input == "2":
			self.login()
		else:
			sys.exit(1000)

	def register(self):
		name = input("Name: ")
		email = input("Email: ")
		password = input("Password: ")

		response = self.db.register(name, email, password)

		if response:
			
obj = Flipkart() 