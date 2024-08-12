"""
main script for specific specie data extract from db to excel
"""
from datetime import datetime

# import custom functions from different files
from read_file_to_array import*
from mysql_to_excel import*
from read_directory import*

directory = os.getcwd() + "\\input\\"
# print(directory)
# sys.exit(0)
# directory = "C:\\Users\\User\\Downloads\\marshmellows_scripts\\sugas_09.03.2022\\input\\"

# gets current date: day, month, year
dt = datetime.now()
date = dt.strftime('%d.%m.%Y')

file_names = file_list(directory)
print(file_names)

i = 0
for name in file_names:

	print('===============    ' + name + '    ================')
	# if i >= 2: # test purpose
	# 	break

	# from file create value array
	values = read_file_to_array(directory, str(name + '.txt'))
	# print(values)

	# make arr as string for Mysql DB
	sql_values = create_str_list(values)
	# print(sql_values) # DO THIS ONLY WITH SMALL DATA LIST
	# sys.exit(0)

	# need to pass 'name' to create excel name

	# run sql and create excel file
	# excel_name, sql_values, limit (10000 normālai pārlasei; 1000 un mazāk testam)
	mysql_to_excel('marshmellows-' + name + '_' + date, sql_values, str(10000))
	i = i + 1