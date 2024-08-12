"""
reads folder files and make list of them in array
"""
import os

def file_list(dir):
	# dir = "C:\\Users\\User\\Downloads\\dabasdati_scripts\\konkrēta suga\\input"
	
	arr = []
	dir_list = os.listdir(dir)
	for d in dir_list:
		# print(d.rsplit('.')[0])
		arr.append(d.rsplit('.')[0])
	# print(arr)
	return arr