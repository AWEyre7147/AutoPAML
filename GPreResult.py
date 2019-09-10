# StatPrelim.py: 
# Input:   
# Output:  

##### FUNCTION #####

def prelim_builder(file_text, pre_results, curr_test):
	i = 0
	pre_results.write("%r\n" % curr_test)
	for line in file_text:															# Prelim result file 
		if line.find("branch ") > -1:												# Retrieves the index values of the lines 
			j = i + 3
			new_line = file_text[j]
			pre_results.write("%r\n" % new_line)
			i = i + 1
		else:
			i = i + 1
			
##### PROGRAM #####

import glob, os

pre_results = file("prelim.txt", 'wt')
paml_folders = glob.glob("*PAML")
curr_dir = os.getcwd()						
pre_dir = os.getcwd() + '\\prelim.txt'

for curr_folder in paml_folders:
	text_file = curr_dir + "\\" + curr_folder + "\\analysis\\output.txt"
	curr_test = curr_folder[:-4]
	file_text = file(text_file).readlines()
	
	prelim_builder(file_text, pre_results, curr_test)