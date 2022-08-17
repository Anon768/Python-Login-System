import json
import mysql.connector
from mysql.connector import cursor

with open("db_info.json", mode="r") as file_json:
	info_db = json.load(file_json)

db = mysql.connector.connect(
	host= info_db["host"],
	user= info_db["user"],
	password= info_db["password"],
	database= info_db["database"]
)

cursor = db.cursor()
