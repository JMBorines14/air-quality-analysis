#rename_files.py is a Python script that changes the filename of the downloaded files to a prescribed format.
#Names of the downloaded files have different format, while unified/uniform formats will be easier to read and iterate
#once they are opened in Jupyter Notebook.

import os

path ="/Users/JMGB/OneDrive - University of the Philippines/CS 132/Project/Project Repository/traffic-data-preprocessing"
dir_list = os.listdir(path)

for i in range(len(dir_list)):
	if dir_list[i] == "rename_files.py":
		continue
	old_file = path + "/" + dir_list[i]
	name, extension = os.path.splitext(old_file)

	file_name = dir_list[i]
	date = file_name[file_name.index('_')+1:]
	
	if '-' in date:
		temp = date.split('-')
		new_file = temp[0] + temp[1] + extension
	elif '_' in date:
		temp = date.split('_')
		new_file = temp[0][:2] + temp[0][2:] + extension
	else:
		new_file = "0603" + extension

	new_file = path + "/" + new_file
	
	os.rename(old_file, new_file)