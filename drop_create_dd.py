"""
drops and recreates database
ONLY RUN IN FOLDER WITH NEW SQL BACKUP FILE
"""
# import the modules
from pymysql import*
from datetime import datetime
import sys, os, re
import pandas.io.sql as sql

# connect the mysql with the python
con=connect(user="root",password="appropriate_password",host="localhost")

try:   
    sql.read_sql("drop database if exists marsmellow_data;",con)
except Exception as e:
    pass
    # print("Unknown error")
    # print(e)

try:
    sql.read_sql("create database marsmellow_data;",con)
except Exception as e:
    pass
    # print("Unknown error")
    # print(e)
con.close()

# recreates database with sql file
file_names = os.listdir(os.getcwd())
# print(file_names)
sql_file = ""

for f in file_names:
	x = re.search(r"^marsmellows_\d{2}_\d{2}_\d{2}\.sql$", f)
	if x:
		# print('yes ' + f)
		sql_file = f
		break
	else:
		pass

try:
    os.system("mysql -u root -p marsmellow_data < " + os.getcwd() + "\\" + sql_file)
except Exception as e:
    pass
    # print("Unknown error")
    print(e)

