# StatPreC.py: 
# Input:   
# Output:  

##### FUNCTION #####

def prestat_builder(file_text, stat_prelim, curr_test):
	i = 0
	stat_prelim.write("%r\n" % curr_test)
	for line in file_text:															# Prelim result file 
		if line.find("lnL") > -1:												# Retrieves the index values of the lines 
			new_line = file_text[i]
			stat_prelim.write("%r\n" % new_line)
			i = i + 1
		else:
			i = i + 1

##### PROGRAM #####

import glob, os

stat_prelim = file("prestat.txt", 'wt')
paml_folders = glob.glob("*PAML")
curr_dir = os.getcwd()

for curr_folder in paml_folders:
	text_file = curr_dir + "\\" + curr_folder + "\\analysis\\output.txt"
	curr_test = curr_folder[:-4]
	file_text = file(text_file).readlines()
	
	prestat_builder(file_text, stat_prelim, curr_test)
