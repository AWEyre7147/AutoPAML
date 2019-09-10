# StatResult.py: 
# Input:   
# Output:  

##### FUNCTION #####

def result_builder(pre_dir, final_results):
	i = 0
	data = ""
	file_text = file(pre_dir).readlines()
	
	for line in file_text:
		line = line.split()
		if len(line) == 1:								# Header Check & Data Reseta
			line = "%s" % line; line = line[3:-3]
			data = ""									
			data = "%s\t" % line
		elif i%6 == 5:									# Final Model Check & Data Writing
			data = data + "%s\n" % line[5]
			final_results.write("%s" % data)
		else:											# Model Ratio Additions
			data = data + "%s\t" % line[5]
		i = i + 1
				
##### PROGRAM #####

import os

final_results = file("model_results.txt", 'wt')
final_results.write("Gene#\tModel 0\tModel 1\tModel 2\tModel 7\tModel 8\n")
pre_dir = os.getcwd() + '\\prelim.txt'

result_builder(pre_dir, final_results)