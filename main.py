from time import strftime as time
import connection as connect
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Login and REgister")
print(ascii_banner)

def register():
	print("Register".center(40, "*"))
	status = True

	while status:
		username = input("Username > ")

		if username == "":
			print("Enter username")
		else:
			age = input("Age > ")

			while status:
				password = input("Password (min 10) > ")
				if password != "" and len(password) >= 10:
					sql_register = "INSERT INTO users(username, age, password, created_on) VALUES (%s, %s, %s, %s)"
					values = (username.replace(" ", "_"), age if age != "" else None, password, time("%Y-%m-%d"))

					connect.cursor.execute(sql_register, values)
					connect.db.commit()

					if connect.cursor:
						print("Account created with Success!")
						status = False
						print("\n")
						login()
					else:
						print("Problem with created account!")
						status = False
				else:
					print("Enter password! The lenght of password must is of at least 10!")

def login():
	print("Login".center(40, "*"))

	while True:
		username = input("Username > ")
		password = input("Password > ")

		if username != 0 and password != 0:
			sql_login = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
			connect.cursor.execute(sql_login)

			result = connect.cursor.fetchone()
			if result:
				print("Login Success! {}".format(username.upper()))
				break
			else:
				print("Nothing account with this credentials!")

		else:
			print("Enter informations!")

while True:
	try:
		print("[1] Register", "[2] Login", "[3] Exit", sep="\n")
		choose = int(input("Choose > "))

		if choose == 1:
			register()
			break
		elif choose == 2:
			login()
			break
		elif choose == 3:
			print("Thank you for using our app!")
			break
		else:
			print("\nSelect a valid Response!")
			continue
	except ValueError as err:
		print("\nYou cans insert only number! {}".format(err))

connect.db.close()