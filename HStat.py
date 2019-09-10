# StatCalc.py: 
# Input:   
# Output:  

##### FUNCTION #####
def result_builder(pre_dir, stat_results):
	i = 0
	data = ""
	file_text = file(pre_dir).readlines()
	
	for line in file_text:
		line = line.split()
		if len(line) == 1:								# Header Check & Data Reset
			line = "%s" % line; line = line[3:-3]
			data = ""									
			data = "%s\t" % line
		elif i%6 == 5:									# Final Model & Data Write
			np = "%s" % line[3]; np = np[:-2]
			data = data + "%s\t%s\n" % (line[4], np)
			stat_results.write("%s" % data)
		elif i%6 == 1:									# Model 0 Skip
			data = data
		else:											# Data Fill
			np = "%s" % line[3]; np = np[:-2]
			data = data + "%s\t%s\t" % (line[4], np)	
		i = i + 1
		
##### PROGRAM #####

import os

stat_results = file("stat_results.txt", 'wt')
stat_results.write("Gene#\tlnL 1\tnp 1\tlnL 2\tnp 2\tlnL 7\tnp 7\tlnL 8\tnp 8\n")
pre_dir = os.getcwd() + '\\prestat.txt'

result_builder(pre_dir, stat_results)